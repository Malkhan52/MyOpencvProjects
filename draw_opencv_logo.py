import numpy as np
import cv2

#create a blank image
image = np.zeros((512,512,3), np.uint8)


#draw a ellipse
cv2.ellipse(image,(310,310),(40,40),0,215,-70,(255,0,0),20)
cv2.ellipse(image,(250,200),(40,40),0,45,-230,(0,0,255),20)
cv2.ellipse(image,(170,310),(40,40),0,5,295,(0,255,0),20)

# adding some text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV',(10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imwrite('draw_opencv_logo.jpg',image)
cv2.imshow('Image with blue Line',image)

cv2.waitKey(0)
cv2.destroyAllWindows()