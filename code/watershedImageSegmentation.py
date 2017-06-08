import numpy as np 
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path To Image")

args=vars(ap.parse_args())
coins=cv2.imread(args["image"])

coins_gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
coins_preprocessed = cv2.GaussianBlur(coins_gray, (5, 5), 0)

# get binary image
_, coins_binary = cv2.threshold(coins_preprocessed, 130, 255, cv2.THRESH_BINARY)

# invert image to get coins
coins_binary = cv2.bitwise_not(coins_binary)


# find contours

(coins_contours,_,_)=cv2.findContours(coins_binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# make copy of image
coins_and_contours = np.copy(coins)

# find contours of large enough area
min_coin_area = 60
large_contours = [cnt for cnt in coins_contours if cv2.contourArea(cnt) > min_coin_area]

# draw contours
cv2.drawContours(coins_and_contours, large_contours, -1, (255,0,0))

# print number of contours
print('number of coins: %d' % len(large_contours))

# create copy of image to draw bounding boxes
bounding_img = np.copy(coins)

# for each contour find bounding box and draw rectangle
for contour in large_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(bounding_img, (x, y), (x + w, y + h), (0, 255, 0), 3)