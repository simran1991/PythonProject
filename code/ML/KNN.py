import numpy as np
from matplotlib import pyplot as plt 
import cv2

#feature set containing (x,y) values for 25 houses/training set
trainData=np.random.randint(0,100,(25,2)).astype(np.float32)
print trainData
print "shape of array is" +str(trainData.shape) 

responses=np.random.randint(0,2,(25,1)).astype(np.float32)
print responses
#print responses.ravel()
#print trainData[1]
#rint responses.ravel()==0

red=trainData[responses.ravel()==0]
print red


blue=trainData[responses.ravel()==1]
print blue

#print red[:,0]
#print red[:,1]

#plotting red houses
plt.scatter(red[:,0],red[:,1],80,'r','^')

#plotting blue houses
plt.scatter(blue[:,0],blue[:,1],80,'b','s')




newComer=np.random.randint(0,100,(1,2)).astype(np.float32)
print "newComer data","\n"
print newComer,"\n"
#plt.scatter(newComer[:,0],newComer[:,1],80,'g','o')


newComer10=np.random.randint(0,100,(10,2)).astype(np.float32)
print "newComer data for 10","\n"
print newComer,"\n"
plt.scatter(newComer[:,0],newComer[:,1],80,'g','o')

knn=cv2.KNearest()
knn.train(trainData,responses)
ret, results, neighbours, dist=knn.find_nearest(newComer,3)
print "result: ", results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist
plt.show()
