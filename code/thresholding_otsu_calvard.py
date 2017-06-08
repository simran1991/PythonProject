import numpy as np 
import argparse
import cv2
import mahotas

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gaussianBlur=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("blurred grayscale",gaussianBlur)
cv2.waitKey(0)

T=mahotas.thresholding.otsu(gray)
print "otsu's threshold value %d" % (T)

thresh=gray.copy()
thresh[thresh>T]=255
thresh[thresh<T]=0

thresh=cv2.bitwise_not(thresh)
cv2.imshow("otsu's thresh",thresh)
cv2.waitKey(0)

T=mahotas.thresholding.rc(gray)
print "Ridler-Calvard threshold value %d" % (T)

thresh=gray.copy()
thresh[thresh>T]=255
thresh[thresh<T]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("Ridler-calvard thresholding",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

