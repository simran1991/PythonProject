import numpy as np 
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original img",img)
cv2.waitKey(0)


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)

lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("l*a*b*",lab)

cv2.waitKey(0)
cv2.destroyAllWindows()