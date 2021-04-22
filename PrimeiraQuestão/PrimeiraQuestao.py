###PrimeiraQuestão################


import cv2

import numpy as np

from matplotlib import pyplot as plt

img=cv2.imread("Primeira.png",0)

kernel=np.ones ((5,5),np.float32)/25

mediana=cv2.medianBlur(img,5)


dst_logo=cv2.filter2D(img,-1,kernel)

gaussiana  =  cv2 . GaussianBlur ( img , ( 5 , 5 ), 0 )

cv2.imshow("Media",dst_logo)
cv2.imshow("Mediana",mediana)
cv2.imshow("Gaussiana",gaussiana)



cv2.waitKey()
cv2.destroyAllWindows()




