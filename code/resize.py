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
print(img.shape[1])

#resizing image to new width
#computing ratio for new width it is new width/old width
r=150.0/img.shape[1]
#lets compute new height now that we know the ratio it will be original height*ratio
h=int(img.shape[0]*r)
dim=(150,h)
resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("resized",resized)
cv2.waitKey(0)
print(resized.shape[0])

#resize imge to new height
resized2=imutils.resize(img,height=50)
cv2.imshow("resized",resized2)
cv2.waitKey(0)
print(resized2.shape[1])

resized3=imutils.resize(img,width=100,height=100)
cv2.imshow("resized",resized3)
cv2.waitKey(0)
print(resized3.shape[1])