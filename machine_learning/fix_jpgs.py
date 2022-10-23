
import json
import os
import cv2
import numpy as np
import pytesseract



folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
for folder in folders:
    count = 0
    if not os.path.isdir(f"num_dataset/{folder}"):
        os.mkdir(f"num_dataset/{folder}")
    for im in os.scandir(f"num_cards/{folder}"):
        if ".DS_Store" not in im.path:
            img = cv2.imread(im.path)
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[1:61, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[2:62, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[3:63, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[4:64, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[5:65, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[6:66, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[7:67, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[8:68, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[9:69, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[10:70, 0:60])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[1:61, 1:61])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[2:62, 2:62])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[3:63, 3:63])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[4:64, 4:64])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[5:65, 5:65])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[6:66, 6:66])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[7:67, 7:67])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[8:68, 8:68])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[9:69, 9:69])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[10:70, 10:70])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 1:61])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 2:62])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 3:63])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 4:64])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 5:65])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 6:66])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 7:67])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 8:68])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 9:69])
            count += 1
            cv2.imwrite(f"num_dataset/{folder}/{count}.jpg", img[0:60, 10:70])



        
