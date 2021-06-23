'''

OpenCV reads image in BGR but, matpotlib reads image in RBG. So, we need to convert it from BGR to RGB first.

'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('standard_test_images/lena.jpg', -1)
cv2.imshow('image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
#plt.xticks([]), plt.yticks([]) # This removes scaling on x tics and y tics.
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

'''

Showing multiple images on same window:



import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.jpg', 0) # Black side, pix. value closer then 0 and white side, closer to 255
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)       # it gives 2 values, ret and thresholded so, we use _
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC) # No change upto px 50 and all 50 after that
_, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)


titles = ['original image', 'Binary', 'binary_inv', 'Trunc', 'ToZero', 'ToZero_Inv']
images = [img, th1, th2, th3, th4, th5]

for i in range(6)
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
 
plt.show()

# Don't use waitkey and destroy.... 

'''

