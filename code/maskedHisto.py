import numpy as np 
import argparse
import cv2
import imutils

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])

mask=np.zeros(img.shape[:2],dtype="uint8")
cv2.rectangle(mask,(150,150),(425,400),255,-1)
cv2.imshow("Mask",mask)

masked=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("Apply mask",masked)

imutils.histogramWithMask(img,"histogramWithMask",mask=mask)
cv2.waitKey(0)