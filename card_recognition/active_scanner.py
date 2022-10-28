
import cv2
import numpy as np
import time
import os
import Cards

from tflite_runtime.interpreter import Interpreter

import VideoStream


### ---- INITIALIZATION ---- ###
# Define constants and initialize variables

## Camera settings
IM_WIDTH = 1280
IM_HEIGHT = 720 
FRAME_RATE = 10

## Initialize calculated frame rate because it's calculated AFTER the first time it's displayed
frame_rate_calc = 1
freq = cv2.getTickFrequency()
TF_MODEL_FILE_PATH = 'model.tflite'
# Allocate tensors
interpreter = Interpreter(model_path=TF_MODEL_FILE_PATH)
interpreter.allocate_tensors()
## Define font to use
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize camera object and video feed from the camera. The video stream is set up
# as a seperate thread that constantly grabs frames from the camera feed. 
# See VideoStream.py for VideoStream class definition
## IF USING USB CAMERA INSTEAD OF PICAMERA,
## CHANGE THE THIRD ARGUMENT FROM 1 TO 2 IN THE FOLLOWING LINE:
videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,0).start()
time.sleep(1) # Give the camera time to warm up


### ---- MAIN LOOP ---- ###
# The main loop repeatedly grabs frames from the video stream
# and processes them to find and identify playing cards.

cam_quit = 0 # Loop control variable

# Begin capturing frames
while cam_quit == 0:

    # Grab frame from video stream
    image = videostream.read()

    # Start timer (for calculating frame rate)
    t1 = cv2.getTickCount()

    # Pre-process camera image (gray, blur, and threshold it)
    # Grayscale
    thresh = Cards.preprocess_image(image)

    cnts_sort, cnt_is_card = Cards.find_cards(thresh)


    # Needed before execution!

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
            _class = class_names[np.argmax(predictions_lite_suit)]
            card.best_suit_match = _class

            if _class in ['boat', 'mermade', 'pirate', 'skull_king']:
                card.best_rank_match = _class
            else:
                method = cv2.TM_CCOEFF_NORMED
                others = ['cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
                max = 0
                max_suit = None
                for file in os.scandir(f"templates/{_class}"):
                    if ".DS_Store" not in file.path:
                        template = cv2.imread(file.path, 0)
                        w, h = template.shape[::-1]
                        
                        # Apply template Matching
                        res = cv2.matchTemplate(card.warp,template,method)
                        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                        if max_val > max:
                            max = max_val
                            max_suit = file.path
                
                card.best_rank_match = max_suit

            image = Cards.draw_results(image, card)

    # Finally, display the image with the identified cards!
    cv2.imshow("Card Detector",image)

    # Calculate framerate
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1
    
    # Poll the keyboard. If 'q' is pressed, exit the main loop.
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        cam_quit = 1
        

# Close all windows and close the PiCamera video stream.
cv2.destroyAllWindows()
videostream.stop()


