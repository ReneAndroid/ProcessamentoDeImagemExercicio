import cv2

import numpy as np

from matplotlib import pyplot as plt




def get_butterworth_filter_high(h,w,cutoff=0.05, order=4):    
    P = h/2
    Q = w/2
    dst = np.zeros((h, w, 2), np.float64)
    for i in range(h):
        for j in range(w):
            r2 = np.sqrt((i-P)**2+(j-Q)**2)            
            if r2 == 0:
                r2 = 1.0
            dst[i,j] =1-( 1/(1+(r2/cutoff)**(2*order)))
    return dst

butter_BPA = get_butterworth_filter_high(4,4)

fshift_BPA = dft_shift*butter_BPA
f_ishift_BPA = np.fft.ifftshift(fshift_BPA)
img_back_BPA = cv2.idft(f_ishift_BPA)
img_back_BPA = cv2.magnitude(img_back_BPA[:,:,0],img_back_BPA[:,:,1])


plt.imshow(magnitude_spectrum, cmap='gray')
plt.set_title('Magnitude Spectrum')
plt.set_axis_off()

plt.imshow(butter_BPA[:,:,0], cmap='gray')
plt.set_title('Filtro')
plt.set_axis_off()

plt.imshow(img_back_BPA, cmap='gray')
plt.set_title('Imagem de Saída')
plt.set_axis_off()
