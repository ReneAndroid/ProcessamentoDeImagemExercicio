import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("Segunda.png",0)



mediana = cv2.medianBlur(img,5)

blurGaussian=cv2.GaussianBlur(mediana,(5,5),7)

cv2.imshow("Janela",blurGaussian)
cv2.imwrite("PrimeiraQuestaoResolvida.jpg",blurGaussian)

#Apliquei a mediana deixando-a suavizada e
#depois a guassiana com o desvio padrão de 7 para distorção




cv2.waitKey()
cv2.destroyAllWindows()

