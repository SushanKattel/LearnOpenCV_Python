'''

Mathematically, circle = (x-h)^2 + (y-k)^2 = r^2
where, (h,k) is the center of the circle, and r is the radius of the circle.

'''


import cv2
import numpy as np

#img = cv2.imread("standard_test_images/BasicShapes.jpg")
img = cv2.imread("standard_test_images/balls.jpg")
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # For canny, gray image is preferred
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
'''
circles = cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]])

image = 8 bit, single channel, grayscale input image.
circles = Output vectors of found circles.
Method = Detection Method, See HoughModes. Currently, the only implemented method is HOUGH_GRADIENT.
dp = Inverse ratio of the accumulator resolution to image resolution. When dp = 1, accumulator has same 
     resolution as the input image and if dp = 2, the accumulator has half as weak as the width and the height
minDist = minimum distance between the centers of the detected circles.
param1 = First method specific parameter. In case of HOUGH_GRADIENT, it is the higher threshold of the two
         passed to the canny edge detector (the lower one is twice smaller).
param2 = Second method specific parameter. In case of HOUGH_GRADIENT, it is the accumulator threshold for 
         the circle centers at the detection stage.
minRadius = Minimum circle radius.
maxRadius = Maximum circle radius. if <= 0, uses the maximum image dimension. If <0, returns centers without 
            finding the radius.

'''
detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x,y), r, (255, 0, 255), 3)
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)  # since 2 is small value,
                                                     # this circle looks like dots and help to show centers 😊


cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()