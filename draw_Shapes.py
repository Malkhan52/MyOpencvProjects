import numpy as np
import cv2

#create a blank image
image = np.zeros((512,512,3), np.uint8)

# draw a diagonal line of width 5px
cv2.line(image,(0,0),(511,511),(255,0,0),5)

#draw rectangle 
cv2.rectangle(image, (384,0),(510,128),(0,255,0),3)

#draw a circle
cv2.circle(image,(447,63),63,(0,0,255),3)

#draw a ellipse
cv2.ellipse(image,(256,256),(100,50),0,0,180,255,-1)

#draw arrowed Line
cv2.arrowedLine(image,(10,510),(50,300),(100,100,100),4,0,1)

#draw marker
cv2.drawMarker(image,(150,20),(0,0,250),1,20,2,8) #4th arg 1 = MARKER_CROSS
#draw marker
cv2.drawMarker(image,(190,20),(0,0,250),2,20,2,8) #4th arg 2 = MARKER_STAR
#draw marker
cv2.drawMarker(image,(230,20),(0,0,250),3,20,2,8) #4th arg 3 = MARKER_DIAMOND
#draw marker
cv2.drawMarker(image,(270,20),(0,0,250),4,20,2,8) #4th arg 4 = MARKER_SQUARE
#draw marker
cv2.drawMarker(image,(310,20),(0,0,250),5,20,2,8) #4th arg 5 = MARKER_TRIANGLE_UP
#draw marker
cv2.drawMarker(image,(350,20),(0,0,250),6,20,2,8) #4th arg 6 = MARKER_TRIANGLE_DOWN
#draw marker
cv2.drawMarker(image,(110,20),(0,0,250),7,20,2,8) #4th arg 7 = MARKER_TILTED_CROSS

# adding some text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV',(10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imwrite('shapes.jpg',image)
cv2.imshow('Image with blue Line',image)

cv2.waitKey(0)
cv2.destroyAllWindows()