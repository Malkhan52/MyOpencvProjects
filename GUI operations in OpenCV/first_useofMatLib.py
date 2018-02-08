import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('girl.jpg',0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on x and y axis
plt.show()

cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()