import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')   # To create a window with a name.

cv.createTrackbar('B', 'image', 0, 255, nothing)  # Name of bar,name of window,StartVal,EndVal,Callback func.
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0:OFF \n 1:ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) &0xFF
    if k == 27:  #ESC key
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]  # Giving BGR values from trackbar to image !

cv.destroyAllWindows()

''' 
Now, As additional task, take a image and convert to Grayscale using trackbar. Also, create other trackbar 
and print the value of trackbar on image !
'''