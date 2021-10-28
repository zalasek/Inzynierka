I=imread('C:\Users\zales\Desktop\POC_2\obrazy_orginal\trojkat.png');


for i=1:1:4
 temp = imresize(I,i);
 temp = crop(temp);
 L1=fftshift(fft2(temp));
 figure(i)
 imshow(temp)
end




function y = crop(img)
 targetSize = [512 512];
 window = centerCropWindow2d(size(img),targetSize);
 y = imcrop(img,window);
end