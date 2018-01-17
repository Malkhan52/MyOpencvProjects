# Author: Malkhan Singh
# email: malkhansinghrathaur@gmail.com
# for starting introduction check here https://docs.opencv.org/3.2.0/dc/d2e/tutorial_py_image_display.html
# source url: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
# date of code writing: Jan,14 2018


import cv2
import numpy

input_image = cv2.imread('girl.jpg')

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

cv2.imwrite("girl_gray_iamge.jpg", gray_image)
cv2.imwrite("girl_hsv_iamge.jpg", hsv_image)

cv2.imshow("Color Image", input_image)
cv2.imshow("Gray Image",gray_image)
cv2.imshow("HSV Image", hsv_image)

cv2.waitKey(0) & 0xFF # 0xff for 64-bit machine
cv2.destroyAllWindows()