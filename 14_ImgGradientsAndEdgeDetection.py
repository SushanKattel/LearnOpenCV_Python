'''

An image gradient is a directional change in the intensity or color in an image. -Wikipedia
There are several methods of image gradients available in opencv but we see three of them here:
 The laplacian derivative, The sovel X method, the sovel Y method.
These are different gradient functions, which uses different mathematical operations to produce the required image.
The laplacian calculates laplacian derivatives whereas shovel is joint gaussian and differentation operation.

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('standard_test_images/lena.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)  #ksize is optional arg. Min. is better
'''
64F is a datatype.
We are using 64 bit float due to the negative slope induced by transforming image from white to black.
This is just a 64 bit float datatype which supports the negative numbers which we wil be dealing with when 
laplacian method is run on our image.
Then we convert it to unsigned 8 bit integer as below:
'''
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)   # 1 = dx, 0 = dy which are order of derivative on x and y
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)   # ksize is opt.

sobelX = np.uint8(np.absolute(sobelX))   # change of intensity in x direction
sobelY = np.uint8(np.absolute(sobelY))   # change of intensity in y direction

# The sodoku image represent it better !

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

canny = cv2.Canny(img, 100, 200)
#see about canny in next program. Now cmt it. Only after next :p

titles = ['image', 'Laplacian','sobelX', 'sobelY', 'sobelCombined', 'canny' ]
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(6):
    plt.subplot(3,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()