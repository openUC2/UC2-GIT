
%%%%% IDT poss after LED Postion calibtion %%%%%

% apply calibrated
 if Calib==1
    Ini_NAx=(freqXY3(:,2)'-(Cablib_Nx/2+1))/Cablib_Nx/Pixelsize;
    Ini_NAy=(freqXY3(:,1)'-(Cablib_Ny/2+1))/Cablib_Ny/Pixelsize;
 else
    TempNA=Ini_NAx;
    Ini_NAx=-Ini_NAy;
    Ini_NAy=TempNA;
 end

% correct frequency coord of LED 
Ini_PixelShiftx=zeros(1,Length_MN);
Ini_PixelShifty=zeros(1,Length_MN);

for i=1:Length_MN
    pic_pos=i;
    
    Ini_PixelShiftx(pic_pos)=round(Ini_NAx(pic_pos)*Pixelsize*Nx);
    Ini_PixelShifty(pic_pos)=round(Ini_NAy(pic_pos)*Pixelsize*Ny);
end

%% Generate Complex or pure phase 3D object, and correspoding intensity bright field iamges

disp('Calculating slice-wise transfer functions...');
PTF_4D=single(zeros(Nx,Ny,length(Depth_Set),Length_MN));
ATF_4D=single(zeros(Nx,Ny,length(Depth_Set),Length_MN));

PTF_3D=single(zeros(Nx,Ny,length(Depth_Set)));
ATF_3D=single(zeros(Nx,Ny,length(Depth_Set)));

%%

uu=fx2D;
vv=fy2D;
k_Wavenum=k;
k_Medium=k_Wavenum*n_Medium;

figure
for i=1:Length_MN
    pic_pos=i
%%
    v_s=Ini_NAx(pic_pos);
    u_s=Ini_NAy(pic_pos);
    
    G = real(1./(k_Medium*sqrt(1-lambda^2.*((uu-u_s).^2+(vv-v_s).^2))));
    Gf = real(1./(k_Medium*sqrt(1-lambda^2.*((uu+u_s).^2+(vv+v_s).^2))));
    %dip_image(G)
    %%
    Pupil = circshift(Aperture_fun,[Ini_PixelShiftx(pic_pos),Ini_PixelShifty(pic_pos)]);
    Pupilf = circshift(Aperture_fun,-[Ini_PixelShiftx(pic_pos),Ini_PixelShifty(pic_pos)]);
    
    uv_vector1=real(sqrt(1-lambda^2.*((uu-u_s).^2+(vv-v_s).^2)));
    uv_vector2=real(sqrt(1-lambda^2.*((uu+u_s).^2+(vv+v_s).^2)));
    uv_s=sqrt(1-lambda^2.*(u_s^2+v_s^2));
    
    for j=1:length(Depth_Set)
        PTF_3D(:,:,j)=...
        (Pupil.*sin(k_Medium.*Depth_Set(j).*(uv_vector1 - uv_s)).*G+...
            Pupilf.*sin(k_Medium.*Depth_Set(j).*(uv_vector2 - uv_s)).*Gf)+...
     1i*(Pupil.*cos(k_Medium.*Depth_Set(j).*(uv_vector1 - uv_s)).*G-...
            Pupilf.*cos(k_Medium.*Depth_Set(j).*(uv_vector2 - uv_s)).*Gf);
    
        ATF_3D(:,:,j)=...
        -(Pupil.*cos(k_Medium.*Depth_Set(j).*(uv_vector1 - uv_s)).*G+...
             Pupilf.*cos(k_Medium.*Depth_Set(j).*(uv_vector2 - uv_s)).*Gf)+...
      1i*(Pupil.*sin(k_Medium.*Depth_Set(j).*(uv_vector1 - uv_s)).*G-...
             Pupilf.*sin(k_Medium.*Depth_Set(j).*(uv_vector2 - uv_s)).*Gf);         
        
        PTF_3D(:,:,j)=fftshift(PTF_3D(:,:,j));
        ATF_3D(:,:,j)=fftshift(ATF_3D(:,:,j));
    end
    PTF_4D(:,:,:,pic_pos)=0.5*dz*k_Wavenum^2.*PTF_3D;
    ATF_4D(:,:,:,pic_pos)=0.5*dz*k_Wavenum^2.*ATF_3D;
end


%% Calculate Eq.(7) and Eq.(8) in paper
sum_PTF = 0;
sum_ATF = 0;

conj_PTF_Iten=0;
conj_ATF_Iten=0;

conj_term1=0;
conj_term2=0;

tic
for i=1:Length_MN
    pic_pos=i;

    Itmp = I_Raw(:,:,pic_pos);        
    Ihat_tmp = fft2((Itmp));

    sum_PTF=sum_PTF+abs(PTF_4D(:,:,:,pic_pos)).^2;
    sum_ATF=sum_ATF+abs(ATF_4D(:,:,:,pic_pos)).^2;

    conj_PTF_Iten=conj_PTF_Iten+conj(PTF_4D(:,:,:,pic_pos)).*repmat(Ihat_tmp,1,1,length(Depth_Set));
    conj_ATF_Iten=conj_ATF_Iten+conj(ATF_4D(:,:,:,pic_pos)).*repmat(Ihat_tmp,1,1,length(Depth_Set));

    conj_term1=conj_term1+conj(PTF_4D(:,:,:,pic_pos)).*ATF_4D(:,:,:,pic_pos);
    conj_term2=conj_term2+conj(ATF_4D(:,:,:,pic_pos)).*PTF_4D(:,:,:,pic_pos);
end


