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

# number of downsampling steps
num_down = 2

# number of bilateral filtering steps
num_bilateral = 7

# main loop
while True:
    # read input webcam stream
    material, frame = capture.read()
    
    # downsample image using Gaussian pyramid
    img_color = frame
    for _ in range(num_down):
       img_color = cv2.pyrDown(img_color)

    # repeatedly apply small bilateral filter instead of
    # applying one large filter
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

    # upsample image to original size
    for _ in range(num_down):
       img_color = cv2.pyrUp(img_color)

    #STEP 2 & 3
    #Use median filter to reduce noise
    # convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    #STEP 4
    #Use adaptive thresholding to create an edge mask
    # detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
       cv2.ADAPTIVE_THRESH_MEAN_C,
       cv2.THRESH_BINARY,
       blockSize=7,
       C=5)

    # Step 5
    # Combine color image with edge mask & display picture
    # convert back to color, bit-AND with color image
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_cartoon = cv2.bitwise_and(img_color, img_edge)
    
    
    # render webcam stream in window
    cv2.imshow('Code Monkey King', frame)        # no effects
    #cv2.imshow('Code Monkey King', img_gray)     # gray scale
    #cv2.imshow('Code Monkey King', img_edge)     # cartoon edges
    #cv2.imshow('Code Monkey King', img_cartoon)  # cartoon 
    
    # handle script exit
    if cv2.waitKey(1) == ord('~'):
        break

# make clean up
capture.release()
cv2.destroyAllWindows()
