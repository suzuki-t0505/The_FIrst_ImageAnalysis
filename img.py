import cv2
import numpy as np
import matplotlib.pyplot as plt

# ヒストグラム
img = cv2.imread('lena.jpg')
color=('b','g','r')
for i,col in enumerate(color):
    histr=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.show()

# 輪郭
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,150,255,0)
img_,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

img_ = cv2.drawContours(img, contours,-1,(0,0,255),3)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
