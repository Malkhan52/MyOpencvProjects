import numpy as np
import cv2

cap = cv2.VideoCapture('NITR_IMUNC_2018.mp4')

while(1):
	
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('Video Frame', gray)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()