# Author: Malkhan Singh
# email: malkhansinghrathaur@gmail.com
# source url: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
# date of code writing: Jan,14 2018

import cv2
import numpy as np
import copy

#cap = cv2.VideoCapture(0)

#while(1) :

#	_, frame = cap.read()
	
frame = cv2.imread('opencv-logo2.png')
	#frame = cv2.imread('opencv-logo2.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

lower_green = np.array([50,100,100]) #hsv_green = cv2.cvtColor(numpy.uint8([[[0,0,255]]]),cv2.COLOR_BGR2HSV)
upper_green = np.array([70,255,255]) # Here we use this command in py command-line to get HSV values for BGR(here for Red)

lower_red = np.array([0,100,100])	# then print(hsv_green) similarly for green use 0,255,0
upper_red = np.array([20,255,255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)


finalMask = copy.copy(mask_blue);
row,col = mask_blue.shape;
for i in range(0,row):
	for j in range(0,col):
		if mask_red[i][j] >= 230:
			mask_blue[i][j] = mask_red[i][j];
		if mask_green[i][j] >= 230:
			mask_blue[i][j] = mask_green[i][j];
	
res1 = cv2.bitwise_and(frame, frame, mask= mask_blue)
#res2 = cv2.bitwise_and(frame, frame, mask= mask_green)
#res3 = cv2.bitwise_and(frame, frame, mask= mask_red)
#Result = cv2.bitwise_and(res1,res2,res3)

#cv2.imshow("Input HSV", hsv)
cv2.imshow("Blue Mask", mask_blue)
cv2.imshow("Red Mask", mask_red)
cv2.imshow("Green Mask", mask_green)
#cv2.imshow("Result Blue", res1)
#cv2.imshow("Result Green", res2)
#cv2.imshow("Result Red", res3)
cv2.imshow("Final Result", res1)
k = cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()

# TODO: Try to track more than one color in same image e.g. Red,Green,Blue