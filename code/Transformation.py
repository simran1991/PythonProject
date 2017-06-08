import argparse
import cv2
import numpy as np
import imutils

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])

shifted=imutils.translate(img,0,100)
cv2.imshow("shifted Down",shifted)
cv2.waitKey(0)


