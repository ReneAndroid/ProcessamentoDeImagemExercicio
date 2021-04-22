import cv2

import numpy as np

from matplotlib import pyplot as plt



def get_butterworth_filter_low(h,w,cutoff=0.05, order=4):    
    P = h/2
    Q = w/2
    dst = np.zeros((h, w, 2), np.float64)
    for i in range(h):
        for j in range(w):
            r2 = np.sqrt((i-P)**2+(j-Q)**2)
            if r2 == 0:
                r2 = 1.0
            dst[i,j] = 1/(1+(r2/cutoff)**(2*order))     
    return dst


img = cv2.imread("Imagem.png",0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
mask_GPB=np.zeros((5,5,2))


butter_BPB = get_butterworth_filter_low(5, 5)


cv2.imshow("Janela",butter_BPB)

cv2.waitkey()
