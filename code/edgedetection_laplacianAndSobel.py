import numpy as np 
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray) 

lap=cv2.Laplacian(gray,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))

cv2.imshow("laplacian gradients",lap)
cv2.waitKey(0)

sobelX=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(gray,cv2.CV_64F,0,1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

sobelCombined=cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("Sobel gradients",sobelCombined)
cv2.waitKey(0)
cv2.destroyAllWindows()