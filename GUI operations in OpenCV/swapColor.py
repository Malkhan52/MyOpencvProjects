import numpy as np
import cv2

im = cv2.imread('press1.png')
im[np.where((im == [255,255,255]).all(axis = 2))] = [0,33,166]
cv2.imwrite('output.png',im)
cv2.imshow('output image',im)

cv2.waitKey(0)
cv2.destroyAllWindows()
