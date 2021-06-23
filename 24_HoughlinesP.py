import cv2
import numpy as np

img = cv2.imread("standard_test_images/sudoku.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # For canny, gray image is preferred
edges = cv2.Canny(gray, 3, 33, apertureSize=3)

cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=80, maxLineGap=10)

'''

rho = Distance resolution of the accumulator in pixels.
theta = Angle resolution of the accumulator in radians.
threshold = Accumulator threshold parameter. Only those lines are returned that get enough votes (>threshold).
minLineLength = Minimum length of line. Line segments shorter than this are rejected.
maxLineGap = Maximum allowed gap between line segments to treat them as a single line.

'''

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()