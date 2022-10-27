
import cv2
import numpy as np
import time
import os

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

