%DOLNOPRZEPUSTOWY
%OBRAZ1
k1=50;
k2=100;

image=imread('C:\Users\zales\Desktop\POC_2\obrazy_orginal\lena.bmp');
L=fftshift(fft2(image));

Nx=size(L,1);
Ny=size(L,2);

mask_1=zeros(Nx,Ny);
mask_2=zeros(Nx,Ny);


figure(75);
subplot(2,5,1);
imshow(image,[]);
xlabel('orginal');
subplot(2,5,6);
imshow(image,[]);
xlabel('orginal');
subplot(2,5,2);
imshow(log(1+abs(L)),[]);
xlabel('widmo mocy');
subplot(2,5,7);
imshow(log(1+abs(L)),[]);
xlabel('widmo mocy');
mask_1(Nx/2-k1:Ny/2+k1,Nx/2-k1:Ny/2+k1)=1;
mask_2(Nx/2-k2:Ny/2+k2,Nx/2-k2:Ny/2+k2)=1;
subplot(2,5,3);
imshow(mask_1);
xlabel('mask_1');
subplot(2,5,4);
imshow(log(1+abs(L.*mask_1)),[]);
xlabel('mask_1*|FFT2|');
subplot(2,5,8);
imshow(mask_2);
xlabel('mask_2');
subplot(2,5,9);
imshow(log(1+abs(L.*mask_2)),[]);
xlabel('mask_2*|FFT2|');
A=ifft2(ifftshift(L.*mask_1/255));
subplot(2,5,5);
imshow(log(1+abs(A)),[]);
xlabel('wynik');
B=ifft2(ifftshift(L.*mask_2));
subplot(2,5,10);
imshow(log(1+abs(B)),[]);
xlabel('wynik');


%%GRNOPRZEPUSTOWY
%OBRAZ1

k1=50;
k2=100;
image=imread('C:\Users\zales\Desktop\POC_2\obrazy_orginal\lena.bmp');
figure(76);
L=fftshift(fft2(image)/255);
Nx=size(L,1);
Ny=size(L,2);
mask_1=ones(Nx,Ny);
mask_2=ones(Nx,Ny);
subplot(2,5,1);
imshow(image,[]);
xlabel('orginal');
subplot(2,5,6);
imshow(image,[]);
xlabel('orginal');
subplot(2,5,2);
imshow(log(1+abs(L)),[]);
xlabel('widmo mocy');
subplot(2,5,7);
imshow(log(1+abs(L)),[]);
xlabel('widmo mocy');
mask_1(Nx/2-k1:Ny/2+k1,Nx/2-k1:Ny/2+k1)=0;
mask_2(Nx/2-k2:Ny/2+k2,Nx/2-k2:Ny/2+k2)=0;
subplot(2,5,3);
imshow(mask_1);
xlabel('mask_1');
subplot(2,5,4);
imshow(log(1+abs(L.*mask_1)),[]);
xlabel('mask_1*|FFT2|');
subplot(2,5,8);
imshow(mask_2);
xlabel('mask_2');
subplot(2,5,9);
imshow(log(1+abs(L.*mask_2)),[]);
xlabel('mask_2*|FFT2|');
A=ifft2(ifftshift(L.*mask_1));
subplot(2,5,5);
imshow(log(1+abs(A)),[]);
xlabel('wynik');
B=ifft2(ifftshift(L.*mask_2));
subplot(2,5,10);
imshow(log(1+abs(B)),[]);
xlabel('wynik');