
%%%%% Illumination Calibration Script %%%%%

% *** Input and output file names *** %
% inFile='data/LED_cheekCell_comp_misaligned_input.mat';
% outFile='data/LED_cheekCell_comp_misaligned_output_selfCal.mat';

% *** Imaging system parameters *** %
% Define:
%   I: image stack, NxNxM (for M images)
%   NA: objective NA
%   mag: total magnification
%   dpix_c: pixel size (um)
%   lambda: imaging wavelength (um)
%   freqUV: expected spatial frequency of illumination (1/um), Mx2, ('x' in
%           column 1, 'y' in column 2)

% selfCal=load(inFile);
% I=selfCal.data;
% NA=selfCal.metadata.objective.na;
% mag=selfCal.metadata.objective.mag*selfCal.metadata.objective.system_mag;
% dpix_c=selfCal.metadata.camera.pixel_size_um;
% lambda=selfCal.metadata.illumination.wavelength_um;
% freqUV=selfCal.metadata.source_list.na_design/lambda;

I=I_Calib;
mag=Mag;
dpix_c=Pixelsize;%6.5;
freqUV=[Ini_NAx',-Ini_NAy'];

% *** Controls for removing outliers *** %
removeOut=1; %Whether you want to remove outliers and extend to darkfield (generally a good idea)
method='rigidScale'; %Option for transformation from original guess to new 
%guess, used to remove outliers that do not fit that transformation. 
%Possibilities are: 'rigid' (rotation and shift),'rigidScale' (rotation, shift, & scale),
%'affine'(rotation, shift, scale, & shear), 'projective'
alpha=2; %Multiplier by stdev to get outliers (usually 2-3)
scale=0.5; %Value between 0.01 and 0.99; what the weight of suspected outliers is multiplied by at each iteration
tol=0.05; %Level where we consider something an outlier (should be low, ~0.05)

% *** Controls for circle-finding *** %
rScan=[5 0.5]; %[+/- to scan, delta(r)] %Radius scan boundaries and granularity
%Row #1 = radius estimation, row #2 = center estimation
thScan=[20 1; 5  0.5]; %Theta scan boundaries and granularity
dScan=[30 1; 5 0.5]; %Distance scan boundaries and granularity
calRad=0; %Whether or not to calibrate the radius (recommended to do so)

%% Functions
F = @(x) fftshift(fft2(ifftshift(x))); %Fourier Transform
Ft = @(x) fftshift(ifft2(ifftshift(x))); %Inverse Fourier Transform

%% Define system
%Set up space
imSz=size(I);
N=imSz(1:2);
numImg=imSz(3);
imSz(3)=[];

tic;

%Define the coordinates in frequency space in terms of pixels and k-space
%(u,v); convert pixel coord to polar (centD, theta); get the conversion
%factor from k-space to pixels (con)
[ freqXY, con, radP, xI, yI, uI, vI, XYmid ] = calCoord(freqUV,imSz,dpix_c,mag, NA, lambda );

%Convert to distance (pixels), theta (degrees) of circle center from center frequency
freqDTh=cart2Pol(freqXY, XYmid);

%Get Fourier space amplitude images that will be processed
sigmaG=2; %Amount of blurring to use in a Gaussian filter (generally = 2 gives good results)
[FIdiv, FIdivG, FI, w_2NA] = calFI(I, xI, yI, XYmid, radP, sigmaG);
%% Identify darkfield
[ DFI ] = calDF( FI, XYmid );
DFI=zeros(Length_MN,1);
%Print number of brightfield and darkfield images
fprintf('%i BF, %i DF\n',sum(~DFI),sum(DFI))

%% Find circles
%Find circles for the brightfield images only
[ freqDTh3, rad_cal] = calCircEdge(FIdivG(:,:,~DFI), I(:,:,~DFI), radP, freqDTh(~DFI,:), XYmid, xI, yI, sigmaG, rScan, thScan, dScan, calRad, con, lambda);

freqDTh2=freqDTh;
freqDTh2(~DFI,:)=freqDTh3; %Replace the brightfield values only

freqXY_noRemoveOut=pol2Cart(freqDTh2,XYmid); %Save the result before removing outliers to compare

if removeOut

    [ freqDTh2 ] = removeOutliers(freqDTh, freqDTh2, XYmid, method,alpha, scale, tol, DFI);
    %When include DFI, it doesn't use the darkfield to fit but it does
    %replaces darkfield with fit values (if you don't include the DFI
    %variable, it does not extend to darkfield)

end

freqXY2=pol2Cart(freqDTh2,XYmid);

%% Format output & save
%Convert back to k-space values
freqUV_cal=(freqXY2-repmat(XYmid,[numImg 1]))./con;
freqUV_noRemoveOut=(freqXY_noRemoveOut-repmat(XYmid,[numImg 1]))./con;
NA_cal=(rad_cal./con).*lambda;
w_NA_cal=double(sqrt(uI.^2 + vI.^2)<rad_cal);

illumNA=lambda.*sqrt(freqUV_cal(:,1).^2 + freqUV_cal(:,2).^2);
[illumNAsorted,illumIdx]=sort(illumNA);
t_cal=toc;

fprintf('Time elapsed: %.3f seconds\n',t_cal)

% Save values
metadata.source_list.na_design=freqUV.*lambda;
metadata.source_list.na_calib=freqUV_cal.*lambda;
metadata.source_list.na_nRO=freqUV_noRemoveOut.*lambda;

metadata.self_cal.na_cal=NA_cal;
metadata.self_cal.time_cal_s=t_cal;
metadata.self_cal.DFI=DFI;


%% Display results
sliderDisplayImVC2(log(abs(FI(:,:,~DFI))), cat(3,[freqXY(~DFI,:) radP.*ones(sum(~DFI),1)],[freqXY2(~DFI,:) rad_cal.*ones(sum(~DFI),1)]),{'caxis([2 6])','title(''Brightfield Only: (red) Uncalibrated, (green) Calibrated'')'}); 

%% Nonlinear fit

D_led=Bright_Radius;
theta_cor=0;%LED position parameter
leddx_cor=0;
leddy_cor=0;
h_err=fDL;
h_cor=h_err;
Q0=[theta_cor,leddx_cor,leddy_cor,h_cor];

Ini_NAx_Ori=(freqXY(:,2)'-(Cablib_Nx/2+1))/con;
Ini_NAy_Ori=(freqXY(:,1)'-(Cablib_Ny/2+1))/con;

Ini_NAx_Cal=(freqXY2(:,2)'-(Cablib_Nx/2+1))/con;
Ini_NAy_Cal=(freqXY2(:,1)'-(Cablib_Ny/2+1))/con;

R=[Sorted_Pos(1,:)',Sorted_Pos(2,:)',Ini_NAx_Cal',Ini_NAy_Cal'];

F=@(Q,R)...
   ((((D_led*cos(pi/180*Q(1)).*R(:,1)-D_led*sin(pi/180*Q(1)).*R(:,2)+Q(2))./ ...
sqrt(((D_led*cos(pi/180*Q(1)).*R(:,1)-D_led*sin(pi/180*Q(1)).*R(:,2)+Q(2))).^2+ ...
      (D_led*sin(pi/180*Q(1)).*R(:,1)+D_led*cos(pi/180*Q(1)).*R(:,2)+Q(3)).^2+Q(4).^2)./lambda)-R(:,3)).^2+...
    (((D_led*sin(pi/180*Q(1)).*R(:,1)+D_led*cos(pi/180*Q(1)).*R(:,2)+Q(3))./ ...
sqrt(((D_led*cos(pi/180*Q(1)).*R(:,1)-D_led*sin(pi/180*Q(1)).*R(:,2)+Q(2))).^2+ ...
      (D_led*sin(pi/180*Q(1)).*R(:,1)+D_led*cos(pi/180*Q(1)).*R(:,2)+Q(3)).^2+Q(4).^2)./lambda)-R(:,4)).^2);       

[a]=nlinfit(R,zeros(size(R,1),1),F,Q0);
Q=a;

% load('LEDPos.mat');
% Q=LEDPos;

Ini_NAx_fit=(D_led*cos(pi/180*Q(1)).*R(:,1)-D_led*sin(pi/180*Q(1)).*R(:,2)+Q(2))./ ...
       sqrt((D_led*cos(pi/180*Q(1)).*R(:,1)-D_led*sin(pi/180*Q(1)).*R(:,2)+Q(2)).^2+ ...
            (D_led*sin(pi/180*Q(1)).*R(:,1)+D_led*cos(pi/180*Q(1)).*R(:,2)+Q(3)).^2+Q(4).^2)./lambda;
Ini_NAx_fit=Ini_NAx_fit';
         
Ini_NAy_fit=(D_led*sin(pi/180*Q(1)).*R(:,1)+D_led*cos(pi/180*Q(1)).*R(:,2)+Q(3))./ ...
       sqrt((D_led*cos(pi/180*Q(1)).*R(:,1)-D_led*sin(pi/180*Q(1)).*R(:,2)+Q(2)).^2+ ...
            (D_led*sin(pi/180*Q(1)).*R(:,1)+D_led*cos(pi/180*Q(1)).*R(:,2)+Q(3)).^2+Q(4).^2)./lambda;
Ini_NAy_fit=Ini_NAy_fit';

freqXY3=[];
freqXY3(:,2)=Ini_NAx_fit'.*con+(Cablib_Nx/2+1);
freqXY3(:,1)=Ini_NAy_fit'.*con+(Cablib_Ny/2+1);

sliderDisplayImVC2(log(abs(FI(:,:,~DFI))), cat(3,[freqXY3(~DFI,:) rad_cal.*ones(sum(~DFI),1)]),{'caxis([2 6])','title(''Brightfield Only: (red) Uncalibrated, (green) Calibrated'')'}); 





