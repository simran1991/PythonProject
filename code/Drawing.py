import numpy as np
import cv2

#creating array of 300x300 with each cell having 24 bits to represet 3 channels
canvas=np.zeros((300,300,3),dtype="uint8")
green=(0,255,0)
#line function first argument is image on which we want to draw
#second arg start coordinate
#third end coordinate
#fourth color
#fifth there is fifth one used for thickness in pixels
cv2.line(canvas,(0,0),(300,300),green,5)


##draw rectangle with four arguments here we pass x,y cordinate for start of rectangle and end x,y coordinate point for end
red=(0,0,255)
cv2.rectangle(canvas,(10,10),(60,60),red,3)

#specify the thickness in negative gives us filles rectanle
red=(0,0,255)
cv2.rectangle(canvas,(200,50),(225,125),red,-3)

cv2.imshow("Draw Line",canvas)
cv2.waitKey(0)