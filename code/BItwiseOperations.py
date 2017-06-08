import numpy as np 
import cv2

rectangle=np.zeros((300,300),dtype="uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)

cv2.imshow("white rectangle",rectangle)
cv2.waitKey(0)

circle=np.zeros((300,300),dtype="uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("white circle",circle)
cv2.waitKey(0)



bitWiseAND=cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND bit wise",bitWiseAND)
cv2.waitKey(0)

bitWiseOR=cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR bit wise",bitWiseOR)
cv2.waitKey(0)

bitwiseXOR=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR bit wise",bitwiseXOR)
cv2.waitKey(0)

bitwiseNOT=cv2.bitwise_not(rectangle,circle)
cv2.imshow("NOT bit wise",bitwiseNOT)
cv2.waitKey(0)
