import numpy as np 
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original img",img)
cv2.waitKey(0)


(b,g,r)=cv2.split(img)

cv2.imshow("Red",r)
cv2.imshow("Blue",b)
cv2.imshow("green",g)
cv2.waitKey(0)

merged=cv2.merge([b,g,r])
cv2.imshow("merged",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()