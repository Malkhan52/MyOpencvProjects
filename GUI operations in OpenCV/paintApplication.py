import cv2
import numpy as np
drawing = False
mode = True
xi,yi = -1,-1
def click_draws(event,x,y,flags,param):
	global ix,iy,drawing,mode,color

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing == True
		ix,iy = x,y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				cv2.line(img,(ix,iy),(x,y),(b,g,r),2*s)
			else:
				cv2.circle(img,(x,y),5,(255,0,0),-1)
			
	elif event == cv2.EVENT_LBUTTONUP:
		drawing == False
		if mode == True:
				cv2.line(img,(ix,iy),(x,y),(b,g,r),2*s)
		else:
				cv2.circle(img,(x,y),2*s,(b,g,r),-1)
	
def nothing(x):
	pass

img = np.zeros((300,512,3), np.uint8)
img[:] = 255
cv2.namedWindow('image')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Press m = to toggle shape,',(10,25), font, 1, (255,255,255), 1, cv2.LINE_AA)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch = 'Brush:'
cv2.createTrackbar(switch,'image',1,5,nothing)

cv2.setMouseCallback('image',click_draws)

while(1):
	cv2.imshow('image',img)
	cv2.imwrite('paintApplication.jpg',img)
	k = cv2.waitKey(1) & 0xff
	if k == 27:
		break
	elif k == ord('m'):
		mode = not mode
	b = cv2.getTrackbarPos('B','image')
	g = cv2.getTrackbarPos('G','image')
	r = cv2.getTrackbarPos('R','image')
	s = cv2.getTrackbarPos(switch,'image')

cv2.destroyAllWindows()