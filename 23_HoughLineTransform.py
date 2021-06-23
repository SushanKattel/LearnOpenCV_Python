'''

The Hough transform is a popular technique to detect any shape, if you can represent that shape in a
mathematical form. It can detect the shape even if it is broken or distorted a little bit.
A line in the image space can be expressed with two variables. For example:
- In the Cartesian co-ordinate system, y = mx + c ( See in MC space also- Point rep. of a line)
- In the polar co-ordinate system, xCos🌐 + ySin🌐 = r  (🌐 = Theta)  ( See in r theta space- Point rep. of a line)
Car. eqn is not able to represent vertical lines so we use polar generally for HoughTransform.
The Hough transform Algorithm has following steps:
1. Edge detection, e.g., using canny
2. Mapping of edge points to a Hough space and storage in an accumulator.
3. Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by
   thesholding and possibly other constraints.
4. Conversion of infinite lines to finite lines.

In openCV, there are two kinds of hough lines transforms:
-> The standard Hough Transform. (HoughLines method)
-> The Probabilistic Hough Line Transform. (HoughLinesP method)

'''

import cv2
import numpy as np

img = cv2.imread("standard_test_images/sudoku.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # For canny, gray image is preferred
edges = cv2.Canny(gray, 3, 33, apertureSize=3)

cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 215)  # lines = cv.HoughLines(image, rho, theta,threshold)
'''

image = source image
lines = Output vector of lines. Each line is represented by a 2 or 3 element vector (rho, theta) or 
        (rho, theta, votes). rho is the distance from the co-ordinate origin (0,0) (top left corner of the image). 
        Theta is the line rotation angle in radians. Votes is the value of accumuator.
rho = Distance resolution of the accumulator in pixels.
theta = Angle resolution of the accumulator in radians.
threshold = Accumulator threshold parameter. Only those lines are returned that get enough votes (>threshold).

These lines will be in polar co-ordinates
'''


for line in lines:
    rho, theta = line[0]
    # Converting polar co-ordinates to cartessian co-ordinates.
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
     # x0 and y0 gives the origin i.e., top left corner of the image
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta)) r = rho
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

Here, the problem is, the drawn lines are of infinite length. i.e., from one corner of image to next corner.
This can be solved using other method. i.e., houghlinesP


'''

