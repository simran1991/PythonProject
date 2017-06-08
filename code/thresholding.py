import numpy as np 
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
(T,thresholdImg)=cv2.threshold(blurred,220,255,cv2.THRESH_BINARY)
cv2.imshow("thresholding binary simple",thresholdImg)
cv2.waitKey(0)

(T,thresholdImgInv)=cv2.threshold(blurred,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresholding Inverse binary simple",thresholdImgInv)
cv2.waitKey(0)

cv2.imshow("after masking",cv2.bitwise_and(img,img,mask=thresholdImgInv))
cv2.waitKey(0)
cv2.destroyAllWindows()