import numpy as np 
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())

img=cv2.imread(args["image"])
cv2.imshow("original img",img)
cv2.waitKey(0)

print(np.uint8([300]))
print("Max value of 255"+str(cv2.add(np.uint8([200]),np.uint8([100]))))

print("Min val of 0"+str(cv2.subtract(np.uint8([50]),np.uint8([100]))))

print("wrap aroung numpy add"+str(np.uint8([200])+np.uint8([100])))
print("wrap around numpy subtract"+str(np.uint8([50])-np.uint8([100])))

M=np.ones(img.shape,dtype="uint8")*200
added=cv2.add(img,M)
cv2.imshow("added img",added)
cv2.waitKey(0)

M=np.ones(img.shape,dtype="uint8")*100
subtracted=cv2.subtract(img,M)
cv2.imshow("subtracted img",subtracted)
cv2.waitKey(0)