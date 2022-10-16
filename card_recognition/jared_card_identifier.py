############## Python-OpenCV Playing Card Detector ###############
#
# Author: Evan Juras
# Date: 9/5/17
# Description: Python script to detect and identify playing cards
# from a PiCamera video feed.
#

# Import necessary packages
import json
import os
import cv2
import numpy as np
import Cards







## Define font to use
font = cv2.FONT_HERSHEY_SIMPLEX
model_dict = {}
cur_int = 0
# Grab frame from video stream
for image_file in os.scandir("card_jpgs/pirate"):
    if ".DS_Store" not in image_file.path:
        image = cv2.imread(image_file.path)
        print(image_file.path)

        # Pre-process camera image (gray, blur, and threshold it)
        image_copy = image.copy()
        
        # Grayscale
        thresh = Cards.preprocess_image(image)
        #cnts_sort, cnt_is_card = Cards.find_cards_debug(thresh, image_copy)
        cnts_sort, cnt_is_card = Cards.find_cards(thresh)


        if len(cnts_sort) != 0:

            # Initialize a new "cards" list to assign the card objects.
            # k indexes the newly made array of cards.
            cards = []
            k = 0

            # For each contour detected:
            for i in range(len(cnts_sort)):
                if (cnt_is_card[i] == 1):
                    # Create a card object from the contour and append it to the list of cards.
                    # preprocess_card function takes the card contour and contour and
                    # determines the cards properties (corner points, etc). It generates a
                    # flattened 200x300 image of the card, and isolates the card's
                    # suit and rank from the image.
                    cards.append(Cards.preprocess_card(cnts_sort[i],image))
            
            for card in cards:
                model_dict[f"{cur_int}_.jpg"] = int(1)
                cv2.imwrite(f"dataset/pirate/{cur_int}_.jpg", card)
                img_rotate_90_counterclockwise = cv2.rotate(card, cv2.ROTATE_180)
                cv2.imwrite(f"dataset/pirate/{cur_int}_I_.jpg", img_rotate_90_counterclockwise)
                cur_int += 1




