clc ;
clear all;
close all;
%Wybieranie i wczytywanie p l i k u
jpg=imread('C:\Users\bartz\Desktop\POC_lab2\auto512.jpg');
% jpg=imread('roska.jpg');
jpg=rgb2gray(jpg);
imshow(jpg);
%dolnoprzepustowy
Hdolno = fspecial( 'gaussian');
%gornoprzepustowy
Hgorno=fspecial('unsharp') ;
lap = [111;1-81;111];
%Fourier
IMGfft=fft2(jpg) ;
%Faza
Phase =fftshift(IMGfft ) ;
%Moc
amplitude = log (1 + abs ( Phase ) ) ;
amplitude = amplitude ./max(max(amplitude ) ) ;
figure ;
imshow(amplitude ) ;
% imsave ;



for i =1:4
jpg=imfilter(jpg, Hgorno ) ;
figure
imshow(jpg) ;
% imsave ;
%Fourier
IMGfft1= fft2(jpg) ;
%Faza
Phase1 = fftshift( IMGfft1 ) ;
%Moc
amplitude = log (1 + abs ( Phase1 ) ) ;
amplitude = amplitude ./max(max(amplitude ) ) ;
figure
imshow(amplitude) ;
% imsave ;
end