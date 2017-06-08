import numpy as np 
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])

cv2.imshow("original",img)
cv2.waitKey(0)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussianBlur=cv2.GaussianBlur(gray,(5,5),0)

canny=cv2.Canny(gaussianBlur,90,140)

cv2.imshow("canny edge",canny)
cv2.waitKey(0)

(cnts,_)=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print "I count %d coins in this image are" % (len(cnts))

coins=img.copy()
cv2.drawContours(coins,cnts,-1,(0,0,255),4)
cv2.imshow("coins detected ",coins)
cv2.waitKey(0)




