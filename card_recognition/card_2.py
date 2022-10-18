
# Import necessary packages
import json
import os
import cv2
import numpy as np
import Cards

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

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
        print(card.warp.shape)
        class_names = ['black', 'boat', 'green', 'mermade', 'pirate', 'purple', 'skull_king', 'yellow']
        #Convert the captured frame into RGB
        #Format for the Mul:0 Tensor
        image_file = "a.jpg"
        cv2.imwrite(image_file, card.warp)
        img = tf.keras.utils.load_img(
            image_file, target_size=(300, 200)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch
        #Expand dimensions to match the 4D Tensor shape.
        TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

        interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
        print(interpreter.get_signature_list())
        classify_lite = interpreter.get_signature_runner('serving_default')

        predictions_lite = classify_lite(sequential_input=img_array)['outputs']
        score_lite = tf.nn.softmax(predictions_lite)


        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
        )
        card.best_rank_match = "none rn"
        card.best_suit_match = class_names[np.argmax(score_lite)]
        image = Cards.draw_results(image, card)
    
    cv2.imshow("final", image)
    cv2.waitKey(0)


                




