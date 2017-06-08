import numpy as np
import cv2

#creating array of 300x300 with each cell having 24 bits to represet 3 channels
canvas=np.zeros((300,300,3),dtype="uint8")
green=(0,255,0)
#center of circle at x=150 and y=150 coordinates
(centerX,centerY)=(canvas.shape[1]/2,canvas.shape[0]/2)

#we draw circle at radius from 0 to 150 at intervals/spacing between each circle as 25
for r in xrange(0,175,25):
	print(r)
	cv2.circle(canvas,(centerX,centerY),r,green)

cv2.imshow("Draw Line",canvas)
cv2.waitKey(0)