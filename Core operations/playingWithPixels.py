import numpy as np
import cv2

img = cv2.imread('girl.jpg')

# px = img[100,100]
# print(px)

# #accessing only blue pixel
# blue = img[100,100,0]
# print(blue)

# img[100,100] = [255,255,255]
# print(img[100,100])

#now same operation using array.item() and array.itemset()
#accessing Red value
print(img.item(100,10,2))
#modifying Red value
img.itemset((100,10,2),100)
print(img.item(100,10,2))
print('Image shape: ',img.shape)
print('Image Size: ',img.size)
print('Image dataType',img.dtype)
eyes = img[80:130,110:150]
img[10:60,10:50] = eyes
cv2.imshow('Image',img)
b,g,r = cv2.split(img) # split() is a costly operation in terms of time, so do it if need, otherwise go for numpy indexing
img = cv2.merge((b,g,r))
# OR
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv2.waitKey(0)
