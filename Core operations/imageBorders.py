import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img = cv2.imread('opencv-logo2.png')

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('BORDER_REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('BORDER_REFLECT')
plt.subplot(234),plt.imshow(reflect_101,'gray'),plt.title('BORDER_REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('BORDER_WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('BORDER_CONSTANT')

plt.show()