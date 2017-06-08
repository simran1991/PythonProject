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

flipped=cv2.flip(img,1)
cv2.imshow("flipped horizontal",flipped)
cv2.waitKey(0)

flipped=cv2.flip(img,0)
cv2.imshow("flipped vertically",flipped)
cv2.waitKey(0)

flipped=cv2.flip(img,-1)
cv2.imshow("flipped both",flipped)
cv2.waitKey(0)