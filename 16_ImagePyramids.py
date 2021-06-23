'''

Till now, we are using images of constant size but sometimes, we have to work with images of different resolutions.
Suppose, I want to search ace inside an image, the faces can be of different sizes. So, using image pyramids,
we just create the images of different resolutions and then we search for the object, (like face) in all of these images.

Pyramid, or pyramid representation is a type of multi scale signal representation in which a signal or image is
subject to repeated smoothing and sub sampling. (Wikipedia)
When we downscale an image in pyramid, it's resolution becomes haf, then 1/4th then, 1/8, then 1/16.. and so on
It is repeated blur and sub sample.
There are two type of image pyramids available in opencv:
1. Gaussian pyramid
2. Laplacian pyramid
Gaussian pyr. is repeated filtering and sub sampling of image. There are two functions available for it:
pir down and pir up.
'''



import cv2
import numpy as np


img = cv2.imread('standard_test_images/lena_color_512.tif')
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# hr1 = cv2.pyrUp(lr2)
# hr2 = cv2.pyrUp(hr1)
#
# cv2.imshow("original image", img)
# cv2.imshow("pirDown1", lr1)
# cv2.imshow("pirDown2", lr2)
# cv2.imshow("pirUp1", hr1)
# cv2.imshow("pirUp2", hr2) # It seems blurred cause, some information is lost during pyrDown.

# Doing this in loop 😊😊😊

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

'''
 Now, for laplacian pyramid, there are no such func. available. A level in Laplacian pyramid is formed by the 
 difference between that level in Gaussian Pyramid and expanded version of it's upper level in Gaussian Pyramid.
 The use of lap. and gau.pyr. is: They helps us to blend the images and helps in reconstruction of the images.
'''
layer = gp[5]
cv2.imshow("UpperLevelGaussianPyramid", layer)
lp = [layer]

for i in range(5,0,-1):  # start, end and steps.
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("OriginalImage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()