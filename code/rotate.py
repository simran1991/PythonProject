import numpy as np 
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())
print(args)
img=cv2.imread(args["image"])
cv2.imshow("original img",img)
cv2.waitKey(0)
print(img.shape)
print(img.shape[:2])
(h,w)=img.shape[:2]
center=(w/2,h/2)

##getRotationMatrix2D have 3 arguments 
#first:point of rotation ie point about which to rotate.
#second : degress to rotaate.
#third :scale of image.

M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(img,M,(w,h))
cv2.imshow("image rotated 45 degs",rotated)
cv2.waitKey(0)

M=cv2.getRotationMatrix2D(center,90,1.0)
rotated=cv2.warpAffine(img,M,(w,h))
cv2.imshow("image rotated 90 degs",rotated)
cv2.waitKey(0)

M=cv2.getRotationMatrix2D(center,-90,0.5)
rotated=cv2.warpAffine(img,M,(w,h))
cv2.imshow("image rotated 90 degs",rotated)
cv2.waitKey(0)

rotated=imutils.rotate(img,75)
cv2.imshow("image rotated 75degs",rotated)
cv2.waitKey(0)