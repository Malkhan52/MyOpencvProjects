import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('girl.jpg',0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

titles = ['Original Image','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TOZERO','THRESH_TOZERO_INV','THRESH_TRUNC']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()

#====================Beacouse of some error this code's output not found=================#