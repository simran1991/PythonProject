import numpy as np 
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original img",img)
cv2.waitKey(0)

img=img[100:300,200:700]

cv2.imshow("cropped img",img)
cv2.waitKey(0)