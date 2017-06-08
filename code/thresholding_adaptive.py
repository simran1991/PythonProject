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
thresholdImg=cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow(" adaptive thresholding using mean",thresholdImg)
cv2.waitKey(0)

thresholdImgInv=cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("adaptive thresholding using Gaussian mean",thresholdImgInv)
cv2.waitKey(0)

cv2.imshow("after masking",cv2.bitwise_and(img,img,mask=thresholdImgInv))
cv2.waitKey(0)
cv2.destroyAllWindows()


