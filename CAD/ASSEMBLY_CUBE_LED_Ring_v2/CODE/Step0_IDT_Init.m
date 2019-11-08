
%% Load measured intensity data and define region for calibration

imSz=size(I_Raw);
Nx=imSz(1);
Ny=imSz(2);
Nz=Nx;

I_Calib=I_Raw(Cablib_pointX-Cablib_Nx/2:Cablib_pointX+Cablib_Nx/2-1,Cablib_pointY-Cablib_Ny/2:Cablib_pointY+Cablib_Ny/2-1,:);

%% Calc the spectrum postion

%Each LED geometric postion
if(0)
    load('Sorted_Pos.mat');
    Pos_X=Sorted_Pos(1,1:Length_MN);
    Pos_Y=Sorted_Pos(2,1:Length_MN);
    clear Sorted_Pos
    Sorted_Pos(1,:)=Pos_X;
    Sorted_Pos(2,:)=Pos_Y;
else
    %% generate coordinates for unit-circle  => 1 = x^2 + y^2
    
    Sorted_Pos_y = sin(linspace(0,2*pi*(1-1/Length_MN),Length_MN)-pi/2+correctionangle);
    Sorted_Pos_x = -cos(linspace(0,2*pi*(1-1/Length_MN),Length_MN)-pi/2+correctionangle);
    Sorted_Pos = vertcat(Sorted_Pos_x, Sorted_Pos_y);
    plot(Sorted_Pos_x,Sorted_Pos_y)
end


% Frequency coordinate
Max_frequency=NA/lambda;
delta_x = 1/(Pixelsize*Nx);      % frequency sampling X.
delta_y = 1/(Pixelsize*Ny);      % frequency sampling Y.
delta_z = 1/(Pixelsize*Nz);      % frequency sampling Z.

fx = (-fix(Nx/2):1:fix((Nx-1)/2))*delta_x; % frequency coordinate X.
fy = (-fix(Ny/2):1:fix((Ny-1)/2))*delta_y; % frequency coordinate Y.
[fx2D, fy2D] = meshgrid(fx,fy);

% Generating coordinates on the surface of Ewald Sphere
fz2D = real(sqrt((n_Medium./lambda).^2-fy2D.^2-fx2D.^2));
[Theta,R] = cart2pol(fx2D,fy2D);
Aperture = ~(R>Max_frequency);
Aperture_fun = double(Aperture);
% figure
% imshow(Aperture_fun)

%%

%initial guess of led postion and frequecy coord
Ini_NAx=zeros(1,Length_MN);
Ini_NAy=zeros(1,Length_MN);
Ini_NAz=zeros(1,Length_MN);

Ini_PixelShiftx=zeros(1,Length_MN);
Ini_PixelShifty=zeros(1,Length_MN);

for i=1:Length_MN
    aii=Sorted_Pos(1,i);
    ajj=Sorted_Pos(2,i);
    pic_pos=i;
    
    Ini_NAx(pic_pos)=(aii.*Bright_Radius)./sqrt((aii.*Bright_Radius)^2+(ajj.*Bright_Radius)^2+fDL^2)/lambda;
    Ini_NAy(pic_pos)=(ajj.*Bright_Radius)./sqrt((aii.*Bright_Radius)^2+(ajj.*Bright_Radius)^2+fDL^2)/lambda;
    Ini_NAz(pic_pos)= real(sqrt((n_Medium/lambda)^2-(Ini_NAx(pic_pos)).^2-(Ini_NAy(pic_pos)).^2));
end


