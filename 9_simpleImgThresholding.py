'''

Thresholdng is a very popular segmentation technique used for separating an object from it's background.
The process of thresholding involvs comparing each pixel of image with a predefined threshold value.
This divides all pix. of input images into 2 groups. First group has pixels having intensity value lower
then the th. and other group has higher values.

'''


import cv2 as cv

img = cv.imread('gradient.jpg', 0) # Black side, pix. value closer then 0 and white side, closer to 255
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)       # it gives 2 values, ret and thresholded so, we use _
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC) # No change upto px 50 and all 50 after that
_, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)



cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)

cv.waitKey(0)
cv.destroyAllWindows()
