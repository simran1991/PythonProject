import argparse
import cv2
#reading custom argument image
ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",help="Path To Image")
args=vars(ap.parse_args())

#reading image
image=cv2.imread(args["image"])

print "width : %d pixels" % (image.shape[1])
print "height : %d pixels" % (image.shape[0])
print "channels: %d channels" %(image.shape[2])

#displaying image
cv2.imshow("Image",image)
cv2.waitKey(0)

#writing image
cv2.imwrite("newTestImage.jpg",image)


#Manipulating pixels
#opencv stores pixes in BGR format not in RBG so take care when using it.

(b,g,r)=image[0,0]
print "Pixel at (0,0) : Red : %d , Green :%d , Blue:%d " % (r,g,b)

image[0,0]=(0,0,255)
(b,g,r)=image[0,0]
print "Altered Pixel at (0,0) : Red : %d , Green :%d , Blue:%d " % (r,g,b)


## now using numpy slicing functionality to grab 100x100 pixels from top left
#numpy expects four argument start Y index ie 0 here,End Y index adnd start X index and End X index
#eg 0:100,0:90 means Y start is 0 and end is 100 and X start is 0 X end is 90

corner=image[0:100,0:100]
cv2.imshow("corner",corner)
cv2.waitKey(0)

##now altering the corner coloring it green
image[0:100,0:100]=(0,255,0)
cv2.imshow("Altered Corner",image)
cv2.waitKey(0)

