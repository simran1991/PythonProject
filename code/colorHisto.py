import numpy as np 
import argparse
import cv2
from matplotlib import pyplot as plt

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])

(b,g,r)=cv2.split(img)

plt.figure()
plt.title("Histogram for grayscale image")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
histB=cv2.calcHist([b],[0],None,[256],[0,256])
plt.plot(histB,color="b")
plt.xlim([0,256])
histG=cv2.calcHist([g],[0],None,[256],[0,256])
plt.plot(histG,color="g")
plt.xlim([0,256])
histG=cv2.calcHist([r],[0],None,[256],[0,256])
plt.plot(histG,color="r")
plt.xlim([0,256])

plt.show()
cv2.imshow("original",img)
cv2.waitKey(0)
