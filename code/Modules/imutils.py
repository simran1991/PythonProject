import numpy as np 
import cv2
from matplotlib import pyplot as plt

def translate(image,x,y):
	M=np.float32([[1,0,x],[0,1,y]])
	shifted=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
	return shifted

#method having two compulsory and two optional arguments
def rotate(image,angle,center=None,scale=1.0):
	(h,w)=image.shape[:2]
	if center is None:
		center=(w/2,h/2)
	M=cv2.getRotationMatrix2D(center,angle,scale)
	rotated=cv2.warpAffine(image,M,(w,h))	
	return rotated

def resize(image,width=None,height=None,inter=cv2.INTER_AREA):
	dim=None
	(h,w)=image.shape[:2]	
	
	if width is None and height is None:
		return image

	if width is None:
		r=height/float(h)
		dim=(int(r*w),height)

	if	height is None:
		r=width/float(w)
		dim=(width,int(r*h))

	resized=cv2.resize(image,dim,interpolation=inter)
	return resized

def histogramWithMask(image,title,mask=None):
	chanels=cv2.split(image)
	colors=("b","g","r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")	

	for (channel,color)	in zip(chanels,colors):
		hist=cv2.calcHist([channel],[0],mask,[256],[0,256])
		plt.plot(hist,color=color)
		plt.xlim([0,256])

	plt.show()		