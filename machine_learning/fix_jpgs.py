
import json
import os
import cv2
import numpy as np
import pytesseract




for im in os.scandir(f"number_model"):
    if ".DS_Store" not in im.path:
        print(im.path)
        img = cv2.imread(im.path)
        text = pytesseract.image_to_string(cropped)
        print(text)
        cv2.imshow("i", img)
        cv2.waitKey(0)

