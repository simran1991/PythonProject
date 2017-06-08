import numpy as np 
import argparse
import cv2
import imutils

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original",img)
#bluring using averaging technique and  kernal size 3x3,5x5 and 7x7 kernal is a sliding wingdow that 
#slides on top of our window from to to bottom and left to right  and pixel at center of this kernal gets average value of surrounding pixels
blurred=np.hstack([cv2.blur(img,(3,3)),cv2.blur(img,(5,5)),cv2.blur(img,(7,7))])

cv2.imshow("average blur",blurred)
cv2.waitKey(0)

#gaussian blur,instead of average or mean of surrounding pixels ,center pixel gets set to value calculated using weighted mean
#pixels closer to center has more weights so we get more natural blur than averaging
gaussian=np.hstack([cv2.GaussianBlur(img,(3,3),0)
					,cv2.GaussianBlur(img,(5,5),0)
					,cv2.GaussianBlur(img,(7,7),0)])

cv2.imshow("gaussian blur",gaussian)
cv2.waitKey(0)

#median blur used to reduce noice in the image ,makes imgae better for edge detection
median=np.hstack([cv2.medianBlur(img,3)
					,cv2.medianBlur(img,5)
					,cv2.medianBlur(img,7)])

cv2.imshow("original",img)
cv2.imshow("median blur",gaussian)
cv2.waitKey(0)



