img=imread('C:\Users\zales\Desktop\POC_2\obrazy_orginal\trojkat.png');

r=100;

[x,y]=size(img);
d1=x/2;
d2=y/2;
mask_d=zeros(x,y);
for i=1:x
     for j=1:y
         if (((i-d1)^2+(j-d2)^2) <= r^2)
         mask_d(i,j)=1;
         end
     end
end
mask_g=1-mask_d;

% imwrite(mask_d,'C:\Users\ignac\OneDrive\Pulpit\studia\semestr 7\POC\Lab 2\zad4\mask_d.png')
% imwrite(mask_g,'C:\Users\ignac\OneDrive\Pulpit\studia\semestr 7\POC\Lab 2\zad4\mask_g.png')
figure
imshow(mask_d)
figure
imshow(mask_g)



temp=fftshift(fft2(img));
widmo_org=uint8(20*log(1+abs(temp)));

dol=temp.*mask_d;
maskaFFT2_d=20*log(1+abs(dol));
wynik_d=uint8(ifft2(ifftshift(dol)));
gor=temp.*mask_g;
maskaFFT2_g=20*log(1+abs(gor));
gor=temp.*maskaFFT2_g;
wynik_g=img+uint8(real(ifft2(ifftshift(gor))));


