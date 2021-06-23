'''

The canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect
a wide range of edges in images. It was developed by John F. Canny in 1986.
The canny edge detection algorithm is composed of five steps:
-> Noise reduction.
-> Gradient Calculation.
-> Non-maximum suppression.
-> Double threshold.
-> Edge Tracking by Hysteresis. (suppressing weak and non connected edges)

'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('standard_test_images/lena.jpg', 0)
img = cv2.imread('D:/yantraDataset/TrainingDataSet/LeftGray/lg.1345.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

canny = cv2.Canny(img, 9, 150) # Threshold are for Hysteresis procedure
# Use trackbar for threshold 1 and threshold 2


titles = ['image', 'Canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# This method gives less noises. Use it with other methods and check.

