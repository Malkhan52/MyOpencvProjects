import cv2
import numpy as np

drawing = False #true if mouse is pressed
mode = True # if true, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
color = -1

#mouse callback function
def click_draws(event,x,y,flags,param):
	global ix,iy,drawing,mode,color

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing == True
		ix,iy = x,y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				if color == 0:
					cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
				elif color == 1:
					cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
				elif color == 2:
					cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
				else:
					cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),2)
			else:
				if color == 0:
					cv2.circle(img,(x,y),5,(255,0,0),-1)
				elif color == 1:
					cv2.circle(img,(x,y),5,(0,255,0),-1)
				elif color == 2:
					cv2.circle(img,(x,y),5,(0,0,255),-1)
				else:
					cv2.circle(img,(x,y),5,(255,255,255),-1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing == False
		if mode == True:
				if color == 0:
					cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),2)
				elif color == 1:
					cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
				elif color == 2:
					cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
				else:
					cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),2)
		else:
				if color == 0:
					cv2.circle(img,(x,y),5,(255,0,0),-1)
				elif color == 1:
					cv2.circle(img,(x,y),5,(0,255,0),-1)
				elif color == 2:
					cv2.circle(img,(x,y),5,(0,0,255),-1)
				else:
					cv2.circle(img,(x,y),5,(255,255,255),-1)
			
img = np.zeros((600,1000,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_draws)

while(1):
# Adding help to toggle shape or change colors
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,'Press m = to toggle shape,',(10,25), font, 1, (255,255,255), 1, cv2.LINE_AA)
	cv2.putText(img,' to change color 0 => Blue, 1=> Green, 2=> Red',(10,60), font, 1,(255,255,255),1, cv2.LINE_AA)
	cv2.imshow('image',img)
	cv2.imwrite('mousePaintingAdvanced3.jpg',img)
	k = cv2.waitKey(1) & 0xff
	if k == ord('0'):
		color = 0
	elif k == ord('1'):
		color = 1
	elif k == ord('2'):
		color = 2
	elif k == ord('m'): # press m to toggle mode
		mode = not mode
	elif k == 27:
		break
cv2.destroyAllWindows()