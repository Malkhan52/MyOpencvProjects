#source url https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_optimization/py_optimization.html 

import cv2
import time

img = cv2.imread('girl.jpg')
e1 = cv2.getTickCount()
#e1 = time.time()
for i in range(5,49,2):
	img = cv2.medianBlur(img,i)
e2 = cv2.getTickCount()
#e2 = time.time()
t = (e2-e1)/cv2.getTickFrequency()
#print(e2-e1)
print(t)