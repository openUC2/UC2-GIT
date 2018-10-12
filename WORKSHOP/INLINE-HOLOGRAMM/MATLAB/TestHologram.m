% read the raw-hologram
myholo = 1.*imread('chip.jpg');
if(0)
    mybak = 1.*imread('test2bg.jpg');
    myholo = myholo./(20+mybak);
end
myholo_b = dip_image(myholo(:,:,2)); % only blue-channel is of interest, because of blue LED
if(1) % eventually crop only a subset of the hologram for speed-purposes
    myholo_b = double(extract(myholo_b , [1024, 1024], [1200, 1400]));
else
    myholo_b = double(myholo);
end

myholo_b = myholo_b./max(max(myholo_b));
% do fourier transform just for presentational purposes
% ft(myholo_b)

% get back amplitude
hologram = sqrt(myholo_b); 

% define acquisition parameters
ps = 1.4e-6;%0.6e-6%.2e-6%3.000e-6;
lambda = 440e-9; % in nanometer %530e-9;

% start and stop z-focus measure
zInFocus = .00145;
zInFocus2 = .00124;

stepsize = 0.0002;

j = 0;
%% Backpropagate the Hologram
% Fresnel Propagation - test out a range of z-values to find the one that
% brings the bug into focus
EF_i = {};
for i = 1:50%a:(b-a)/c:b
    %     [Ef, H] = fresnelprop(hologram,lambda,i,ps);
    zpos = i*stepsize;
    [Ef] = FresnelPropagator(hologram, ps, lambda, zpos);
    %   autofocus(imadjust(EF.^2), 'GDER')
    EF_i{i} = Ef;
    
    disp(i)
    
    
    if(0)
        save_path = strcat(path, filename, 'result1', num2str(j), '_', num2str(zpos), extension);
        j= j+1
        Ef = abs(Ef).^2-min(min(abs(Ef).^2));
        Ef = Ef./max(max(Ef));
        imwrite(Ef, save_path);
    end
    
end
%dip_image(EF_i{19})

holo_result = abssqr(cat(3, EF_i{:}));
return
save 'chip.5' 'holo_result' '-v7.3'


