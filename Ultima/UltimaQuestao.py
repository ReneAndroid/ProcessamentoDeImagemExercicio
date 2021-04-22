#Ultima questão
import cv2
import numpy as np

from matplotlib import pyplot as plt


img=cv2.imread("Ultima.png",0)
imgneg=255-img


Limiar,imgLimiar=cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)

cv2.imshow("janela",imgLimiar)

cheque = cv2.imread('Ultima.png',0)
kernel = np.array([[0,0,0],[1,1,1],[0,0,0]], np.uint8)
dilation = cv2.dilate(imgLimiar,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)




cv2.imshow("janela",imgLimiar)
cv2.imshow("JanelaDilatação",dilation)
cv2.imshow("janelaErosa",erosion)
cv2.imshow("Final",mediana)


