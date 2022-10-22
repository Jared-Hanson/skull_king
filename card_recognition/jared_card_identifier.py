
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
cn = 0
# Grab frame from video stream
folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

for im in os.scandir(f"num_cards"):
    print(im.path)
    image = cv2.imread(im.path)

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
            class_names = ['black', 'boat', 'green', 'mermade', 'pirate', 'purple', 'skull_king', 'yellow']
            #Convert the captured frame into RGB
            #Format for the Mul:0 Tensor

            top_corner = card.warp[0:70, 0:70]
            #cv2.imshow("img", top_corner)
            #cv2.waitKey(0)
            cv2.imwrite(f"number_model/{cn}.jpg", top_corner)
            cn += 1

        


                




