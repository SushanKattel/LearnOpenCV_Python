'''

Morphological Transformations are some simple operations based on the image shape.
Morphological Transformations are normally performed on binary images.
A kernel tells you how to change the value of any given pixel by combining it with different amounts of the
neighboring pixels.
As we perform this on binary images, we first create mask.

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('standard_test_images/ballsJPG.jpg', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# This makes image more fine. i.e., the black dots on masked images is removed.
#More big rectangle kernal, more fine, but larger may cause problem.i.e., size of ball might increase.

kernal = np.ones((2,2), np.uint8) # 2*2 square shape is our kernal
dilation = cv2.dilate(mask, kernal, iterations=3)
# A kernal is normally a square or some shape which we want to apply on the image.

#erosen removes boundry of objects. If all the pixels under kernal are 1, then only the pixel is 1.
# Else, the pixel is eroded !

erosion = cv2.erode(mask, kernal, iterations=5)

#Opening is erosion followed by dilation !
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

#In closing, dilation is followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

#Diff. between dilation and erosion of an image.
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

#Diff. between image and opening of an image.
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]



for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()