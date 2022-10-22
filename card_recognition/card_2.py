
# Import necessary packages
import json
import os
import cv2
import numpy as np
import Cards


from tflite_runtime.interpreter import Interpreter

import keras_ocr


import PIL



## Define font to use
font = cv2.FONT_HERSHEY_SIMPLEX
model_dict = {}
cur_int = 0
# Grab frame from video stream

image = cv2.imread("images_of_cards/IMG_6486.jpg")
# Pre-process camera image (gray, blur, and threshold it)
image_copy = image.copy()
# Grayscale
thresh = Cards.preprocess_image(image)
#cnts_sort, cnt_is_card = Cards.find_cards_debug(thresh, image_copy)
cnts_sort, cnt_is_card = Cards.find_cards(thresh)


TF_MODEL_FILE_PATH = 'model.tflite'
TF_NUM_MODEL_FILE_PATH = 'lite-model_keras-ocr_float16_2.tflite'
# Allocate tensors
interpreter = Interpreter(model_path=TF_MODEL_FILE_PATH)
interpreter.allocate_tensors()  # Needed before execution!

interpreter_num = Interpreter(model_path=TF_NUM_MODEL_FILE_PATH)
interpreter_num.allocate_tensors()  # Needed before execution!
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

        gray = cv2.cvtColor(card.warp,cv2.COLOR_GRAY2BGR)
        x = np.asarray(gray, dtype='float32')
        image_data = np.expand_dims(x, 0)
        class_names = ['black', 'boat', 'green', 'mermade', 'pirate', 'purple', 'skull_king', 'yellow']
        print(interpreter.get_signature_list())
        classify_lite = interpreter.get_signature_runner('serving_default')
        predictions_lite_suit = classify_lite(sequential_input=image_data)['outputs']

        c = card.warp[0:70, 0:70]
        retval, c = cv2.threshold(c,210,255,cv2.THRESH_BINARY)
        if np.average(c[20:50, 20:50]) > 70:
            c = ~c
        gray = cv2.cvtColor(c[20:50, 20:50],cv2.COLOR_GRAY2BGR)
        x = np.asarray(gray, dtype='float32')
        image_data = np.expand_dims(x, 0)
        num_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
        print(interpreter_num.get_signature_list())
        classify_lite = interpreter_num.get_signature_runner('serving_default')
        predictions_lite_num = classify_lite(sequential_input=image_data)['outputs']
        
        
        
        card.best_rank_match = num_names[np.argmax(predictions_lite_num)]
        card.best_suit_match = class_names[np.argmax(predictions_lite_suit)]
        image = Cards.draw_results(image, card)
    
    cv2.imshow("final", image)
    cv2.waitKey(0)


                




