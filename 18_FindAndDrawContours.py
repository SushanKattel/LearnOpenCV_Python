'''

Contours can be explained as the curves joining all the continious points along the boundary which are having
same colour or intensity. The contours can be useful tool for shape analysis, object detection, or obj. recog.
For better accuracy, we generally use binary images for finding the contours.
First, we make binary image. Then, before finding out contours, we are going to apply the threshold or
canny edge detection.

'''

import cv2
import numpy as np

#img = cv2.imread('standard_test_images/openCV.png')
img = cv2.imread('D:/yantraDataset/TrainingDataSet/LeftGray/lg.1316.jpg')
img = cv2.resize(img, (512, 512))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
ret, thresh = cv2.threshold(imgGray, 69, 200, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
'''
contours is a python list of all the contours in the image. Each individual contour is a Numpy array 
of (x,y) coordinates of boundary points of the object.
The hierarchy is optional output vector which contains info about image topology and we will see it later !
'''
print("Number of contours = " + str(len(contours)))
#print(contours[0])

cv2.drawContours(img, contours, -1, (255,0,255), 3) # -1 means all contours, next is color and next is thickness
#cv2.drawContours(img, contours, 0, (255,0,255), 3)  # Check one by one changing 0 to 9
cv2.imshow("original", img)
#cv2.imshow("originalGray", imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()