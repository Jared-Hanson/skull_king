


import cv2

image = cv2.imread('test.JPG')
blur = cv2.pyrMeanShiftFiltering(image, 11, 21)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.015 * peri, True)
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(image,(x,y),(x+w,y+h),(36,255,12),2)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.imshow('image', image)
cv2.waitKey(0)