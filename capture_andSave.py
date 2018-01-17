#some video fourcc problem in saving video

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*DIVX)
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))

while(cap.isOpend()) :
	ret, frame = cap.read()
	if ret== True :
		frame = cv2.flip(frame,0)
		out.write(frame)

		cv2.imshow('Flipped frame',frame)
		if cv2.waitKey(1) & 0xff == ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()
	