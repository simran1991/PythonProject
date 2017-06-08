import numpy as np 
import argparse
import cv2
from matplotlib import pyplot as plt

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("original img",gray)
cv2.waitKey(0)

hist=cv2.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("Histogram for grayscale image")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

#equalize histogram is a technique used for grayscale image to enhance contrast of image
equalize=cv2.equalizeHist(gray)
cv2.imshow("original img",gray)
cv2.imshow("equalized Histo",equalize)

cv2.waitKey(0)
cv2.destroyAllWindows()

