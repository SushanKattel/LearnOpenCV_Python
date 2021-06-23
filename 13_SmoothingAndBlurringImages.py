'''

We use this to remove noises in the images.
We can use diverse linear filters for it as linear filters are easy to use.
There are various filters available in open CV:
Homogeneous Filter, Gaussian Filter, Median filter, Bilateral Filter.

Homogeneous filter is the most simple filter, each output pixel is the mean of it's kernel neighbours.
Acc. to Wikipedia.org, In image processing, a kernel, convolution matrix, or mask is a small
matrix. It is used for blurring, sharpening, embossing, edge detection, and more.
Homogeneous filter have equal weights, so, they are called homogeneous !

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('standard_test_images/ballsJPG.jpg')
img = cv2.imread('standard_test_images/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
'''
About Kernel:
           -              -
          | 1  1  1  1  1  |
      1   | 1  1  1  1  1  |
k =  ---  | 1  1  1  1  1  |
     25   | 1  1  1  1  1  |
          | 1  1  1  1  1  |
           -              -

Cause, 5*5 is 25 and we have to make matrix of 1. So, we divide by 25 ( divide by width*height 😊)
'''
#Cause, 5*5 is 25
dst = cv2.filter2D(img, -1, kernel)


'''
As in one-dimensional signals, images also can be filtered with various low-pass filters(LPF), high-pass filters(HPF)
etc.
-> LPF helps in removing noises, blurring the images.
-> HPF filters helps in finding edges in the images.
'''
# This is averaging method of bluring
blur = cv2.blur(img, (5,5)) #5,5 is kernel size

#This is gaussian filter Algorithm:
'''
Gaussian filter is nothing but using different weight kernel, in both x and y direction

           -                   -
          | 1   4   6   4   1  |
    1     | 4  16  24  16   4  |
   ---    | 6  24  36  24   6  |
   16     | 4  16  24  16   4  |
          | 1   4   6   4   1  |
           -                   -
   
 Pixel located at middle of kernel have higher weight and the weight decreases with distance from the 
 neighbourhood center. Pixel located on the side have smaller weight and the pixel at center have higher weight.
 When we take 5 by 5 kernel, the result look like above matrix image.
 This is designed to remove high frequency noise from the image. 
 
'''
gblur = cv2.GaussianBlur(img, (5,5), 0)

'''

Median filter is something that replace each pixel's value with the median of it's neighboring pixels.
This method is great when dealing with "salt and pepper noise" (See wikipedia about this noise 😅😂.
NOTE: The kernel size must be odd here, except 1 !

'''
median = cv2.medianBlur(img, 5)

'''

By using all these filters, we not only dissolve the noise, but we also smooth the edges.
Sometimes, we need to preserve the edges, sharply  even the image is blurred. 
So, we use bilateral filter.
First arg. is image, sec. arg. is the diameter of each pixel neighbourhood that is used during the filter,
third arg. is sigma color, fourth arg. is sigma space. See wikipedia for more about bilateral filter.

'''
bilF = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'Gblur', 'MedianBlur', 'BilateralFilter ']
images = [img, dst, blur, gblur, median, bilF]

for i in range(6):
    plt.subplot(3,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

