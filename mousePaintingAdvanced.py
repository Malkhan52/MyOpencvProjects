import cv2
import numpy as np

#mouse callback function
def click_draws(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),10,(x,y),(255,0,0),-1)
