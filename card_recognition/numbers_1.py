# Import necessary packages
import json
import os
import numpy as np
import cv2



BKG_THRESH = 60
model_dict = {}
cur_int = 0
# Grab frame from video stream

image = cv2.imread("0_.jpg")

# Pre-process camera image (gray, blur, and threshold it)
image_copy = image.copy()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
top_corner = gray[0:75, 0:75]

cv2.imshow("thres", top_corner)
cv2.waitKey(0)

retval, thresh = cv2.threshold(top_corner,210,255,cv2.THRESH_BINARY)
cv2.imshow("thres", thresh)
cv2.waitKey(0)

