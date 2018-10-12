% FRESNEL PROPAGATOR

% function [Ef,x,y,G,E0fft,fx,fy,H,indx] = FresnelPropagator(E0, ps, lambda, z, background)
%
% This function computes the double-slit diffraction pattern using the 
% Fresnel Approximation. This code was modified from Dan and Aamod's
% Fresnel propagator codes.
%
% Parameters: E0 - initial complex field in x-y source plane
%             ps - pixel size in microns
%             lambda - wavelength in nm
%             z - z-value (distance from sensor to object)
%             background - optional background image to divide out from
%                          input field
%
% Returns: Ef - 
%          x - 
%          y - 
%          G - 
%          E0fft - 
%          fx - 
%          fy - 
%          H - 
%
function [Ef] = FresnelPropagator(E0, ps, lambda, z)


if size(E0,1) ~= size(E0,2) % Check if image is already square
    
    n = 2048;   % Should be radix 2 (2^n)
    
    if size(E0,1) < n || size(E0,2) < n
        n = min(size(E0,1), size(E0,2));
    end
    
    % Crop image to square at center of image
    widthCrop = ((size(E0,2) - n) / 2) + 1;
    heightCrop = ((size(E0,1) - n) / 2) + 1;
    E0 = E0(heightCrop:heightCrop+(n-1), widthCrop:widthCrop+(n-1));
    
end


% Function handles for Fourier transform and inverse fourier transform
%F = @(x) ifftshift(fft2(fftshift(x)));     % from Lei
%Ft = @(x) ifftshift(ifft2(fftshift(x)));   % from Lei

% Defines a function called FT(), Ift()
Ft = @(x) fftshift(fft2(x));                % Fourier transform and shift
Ift = @(x) ifft2(ifftshift(x));             % Inverse transform and shift
%http://stackoverflow.com/questions/20971945/fresnel-diffraction-in-two-steps
%: U = ifft2(ifftshift(O.*H))

upsample_scale = 1;                 % Scale by which to upsample image
n = upsample_scale * size(E0, 2);   % Image width in pixels (same as height)
grid_size = ps * n;                 % Grid size in x-direction

% Set up grid of equally-spaced points
x = linspace(-grid_size/2, grid_size/2, n);
y = linspace(-grid_size/2, grid_size/2, n);

% Inverse space
fx = linspace(-(n-1)/2*(1/grid_size), (n-1)/2*(1/grid_size), n);
fy = linspace(-(n-1)/2*(1/grid_size), (n-1)/2*(1/grid_size), n);
Fx = repmat(fx, n, 1);
Fy = repmat(fy', 1, n);

% Fresnel kernel / point spread function h = H(kx, ky)
% from Fourier Optics, chapter 4
% H = sqrt(z*lambda)*exp(1i*pi*lambda*z*(Fx.^2+Fy.^2));
%sphere=exp(i*k/2/zc*(xx.^2+yy.^2));
H = exp(1i*(2*pi / lambda) * z)*exp(1i*pi*lambda*z*(Fx.^2+Fy.^2));
%H= cos(pi*lambda*z*(Fx.^2+Fy.^2)+(2*pi*z)/lambda)+1i.*sin(pi*lambda*z*(Fx.^2+Fy.^2)+(2*pi*z)/lambda);

% Compute FFT centered about 0
E0fft = Ft((E0));     % Centered about 0 since fx and fy centered about 0

% Upsample input field by padding image with zeros
padding = floor((n - (n/upsample_scale)) / 2);  % Amount of padding
if(0)
    E0fft = padarray(E0fft, [padding,padding]);     % Pad array with zeros
end


G = H .* E0fft;
Ef = Ift(G);                 % Output after deshifting Fourier transform

end