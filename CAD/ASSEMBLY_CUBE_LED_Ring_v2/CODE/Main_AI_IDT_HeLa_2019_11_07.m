addpath('functions')
addpath('Utilities')

%% Parameter
lambda=0.515; % Wavelength
k=2*pi/lambda; % Wave number

Mag = 1;
NA= 0.3;
subsampling_factor = 1;
Pixelsize = 1*.243; %2362.727pixels == 0.52mm (from measurement);
%Pixelsize = Pixelsize_raw*1e6; %needs to be in µm
n_Medium=1.33;

Length_MN=16;% the number of LEDs
Bright_Radius=35.7;% the Radius of LED ring

fDL=Bright_Radius./tan(asin(NA))% the distance of LED and object
Calib=1; % if Calibrate LED postion
gpu = 0;% if using gpu

correctionangle = 25/180*pi

mysize = 512; % cropsize
%% Step Load measured intensity data and initial spectrum postion
myfilepath = '/Users/bene/Dropbox/Dokumente/Promotion/PROJECTS/UC2/18_PROJECTS/05_QPI_RingLED_Tian/2019_11_07-HeLa/I_obj/I_obj (19).tif_stack.tif';
I_Raw = readtimeseries(myfilepath);
I_Raw = I_Raw(:,:,0:end-2);
I_Raw_filtered = I_Raw/gaussf(I_Raw, 9);

%abs(ft2d(dip_image(I_Raw_filtered)))^.2

%%
I_Raw_filtered = I_Raw_filtered-mean(I_Raw_filtered);
I_Raw_filtered = double(I_Raw_filtered);
I_Raw_filtered = flip(I_Raw_filtered, 3); % wrong order 
I_Raw = circshift(I_Raw_filtered,-5-8,3); % shift it so that the first image is illuminated from below (6 o clock) 

Cablib_Nx=mysize/2;
Cablib_Ny=mysize/2;

Cablib_pointX=size(I_Raw,2)/2;
Cablib_pointY=size(I_Raw,1)/2;

eval Step0_IDT_Init

% Step Implete the calibation of LED postion
if Calib==1
    eval Step1_IDT_Calib
end

%% Implete the IDT
dz=1;
Depth_Set=[-14:dz:14];


eval Step2_IDT_Poss

%% Regularize the result 

Alpha=1e2;
Beta=1e2;

eval Step3_IDT_Reg
% show RI Slice
dip_image(RI)
RI_real = double(real(RI));
RI_imag = double(imag(RI));
save('2019_10_23-HeLa.h5', 'RI_real', 'RI_imag', '-v7.3')


%%
figure
for ii=1:length(Depth_Set)
    subplot(121)
    imshow(imag(squeeze(RI(:,:,ii))),[]);
    subplot(122)
    imshow(real(squeeze(RI(:,:,ii))),[]);
    pause(0.5);
end

