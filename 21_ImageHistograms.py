'''

Histogram is a graph or plot which gives oral idea about intensity distribution of image.
We can get intuition about constrast, brightness, intensity distribution of the image by looking hist.
There are several ways of finding histogram of images. Lets see them below 😊

Histogram can tell weather the image has been properly exposed, weather lightning conditon was light or harsh,
making adjustments for digital images, etc.
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = np.zeros((200, 200), np.uint8)
cv.rectangle(img, (0,100), (150, 200), (255), -1)
cv.rectangle(img, (0,50), (100, 100), (127), -1)

cv.imshow("img", imgA)
# Usng Matplotlib
plt.hist(img.ravel(), 256, [0, 256]) # 256 is max. of pixel value and list is range.
plt.show() # y-axis = total no. of pixels, x-axis = intensity



cv.waitKey(0)
cv.destroyAllWindows()



'''
 # Use this second time 😊 For BGR images
imgA = cv.imread('standard_test_images/lena.jpg')

b, g, r = cv.split(imgA)
cv.imshow("imgA", imgA)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

plt.show()

--------------------


# Using OpenCV
imgB = cv.imread('standard_test_images/lena.jpg', 0)

histB = cv.calcHist([imgB], [0], None, [256], [0, 256])  # [0] for greyscale channel, None is given for full image mask, [256] is histCount and rage is 0 to 256
plt.plot(histB)
cv.imshow("img", imgB)
'''