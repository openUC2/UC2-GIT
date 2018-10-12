% Bug hologram program to demonstrate the magic of Fresnel Propagation

%clear all, clc, close all   % Clear everything each run

path = 'C:\Users\Bene\Downloads\'
path = '/Users/Bene/Downloads/'

filename = 'cam3'
extension = '.jpg';

image_path = [path filename extension]
%image_path = 'C:\Users\Bene\Downloads\RasPi\Holo\148.jpg';%strcat(path, filename, extension);


hologram = imread(image_path);
hologram = im2double(hologram(1:1944, 1:1944,3));



LEN = 333;
THETA = 333;
PSF = fspecial('gaussian', LEN, THETA);
background = imfilter(hologram, PSF, 'conv', 'circular');
hologram = sqrt(hologram./background);

ps = 2e-6%0.6e-6%.2e-6%3.000e-6;
lambda = 440e-9%530e-9;

zInFocus = .00145;
zInFocus2 = .00124;


a = 0.00005;%10e-6;          % Starting z-value
b = 0.009;%100e-4;         % Ending z-value
c = 20;             % Number of steps

stepsize = 0.0003;
result = linspace( 1, c , c)

j = 0;
%% Fresnel Propagation - test out a range of z-values to find the one that
% brings the bug into focus
for i = 1:50%a:(b-a)/c:b
    %     [Ef, H] = fresnelprop(hologram,lambda,i,ps);
    zpos = a+i*stepsize;
    [Ef] = FresnelPropagator(hologram, ps, lambda, zpos);
    %   autofocus(imadjust(EF.^2), 'GDER')
    %dip_image(Ef)
    save_path = strcat(path, filename, 'result1', num2str(j), '_', num2str(zpos), extension);
    j= j+1
    Ef = abs(Ef).^2-min(min(abs(Ef).^2));
    Ef = Ef./max(max(Ef));
    %imwrite(Ef, save_path);
    EF_i{i} = Ef;
end

dip_image(cat(3, EF_i{:})


