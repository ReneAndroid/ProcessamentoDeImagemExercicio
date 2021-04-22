import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem= cv2.imread("Terceira.png")

laplacian=cv2.Laplacian(imagem,cv2.CV_64F)
soblex=cv2.Sobel(imagem,cv2.CV_64F,1,0,ksize=5)
sobley=cv2.Sobel(imagem,cv2.CV_64F,0,1,ksize=5)


cv2.imshow("janela1",laplacian)

cv2.imshow("janela2",soblex)

cv2.imshow("janela3",sobley)



cv2.waitKey()
