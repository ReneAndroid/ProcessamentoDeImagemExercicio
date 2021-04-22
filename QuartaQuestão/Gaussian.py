import cv2

import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("Imagem.png",0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
mask_GPB=np.zeros((5,5,2))

ksize=5

fil_GPB=cv2.getGaussianKernel(5,50)
fil_GPB=fil_GPB*fil_GPB.T

mask_GPB[:,:,0] =fil_GPB
mask_GPB[:,:,1] =fil_GPB


plt.subplot(121)
plt.imshow(fil_GPB, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum')
plt.xticks([]), plt.yticks([])
plt.show()


