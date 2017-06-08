import cv2
import numpy as np
from matplotlib import pyplot as plt

def arrayInfo(array):
	print "shape: "+str(array.shape)
	print "dimension: "+str(array.ndim)
	print "size: "+str(array.size)

img =cv2.imread('digits.png')
cv2.imshow("img",img)
cv2.waitKey(0)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#arrayInfo(gray)
print gray[2,3]
cellH=np.hsplit(gray,100)
#arrayInfo(np.array(cellH))
cellV=np.vsplit(gray,50)
arrayInfo(np.array(cellV))
cells=[np.hsplit(row,100) for row in np.vsplit(gray,50)]

x=np.array(cells)
arrayInfo(x)

train=x[:,:50].reshape(-1,400).astype(np.float32)
test=x[:,:50:100].reshape(-1,400).astype(np.float32)



