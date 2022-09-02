#!/usr/bin/python3

############################################
#
# Simple script to display web camera view
#     for the video tutorial recording
#                 purposes
#
#                    by
#
#             Code Monkey King
#
############################################

# import package
import cv2
import numpy as np

# init webcam capture stream
capture = cv2.VideoCapture(0)

# window size
WIDTH = 320 # 160
HEIGHT = 240 # 120

# set resolution
capture.set(3, WIDTH) # 160
capture.set(4, HEIGHT) # 120

# create output window
cv2.namedWindow('Code Monkey King', flags=cv2.WINDOW_GUI_NORMAL)

# set window size
cv2.resizeWindow('Code Monkey King', WIDTH, HEIGHT)
    
# main loop
while True:
    # read input webcam stream
    material, frame = capture.read()    
        
    # render webcam stream in window
    if material:
        try: cv2.imshow('Code Monkey King', frame)
        except Exception as e: print(e)
    
    # handle script exit
    if cv2.waitKey(1) == ord('~'):
        break

# make clean up
capture.release()
cv2.destroyAllWindows()
