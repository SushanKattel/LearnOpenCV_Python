'''

It is a method of searching and finding a template image inside a larger image.

'''

import numpy as np
import cv2


img = cv2.imread('standard_test_images/BasicShapes.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('standard_test_images/template2.jpg', 0)


res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)   #See doc. of opencv for various template matching operations
print(res)
# Here we see diff points in matrix. The brightest point is the topLeft corner of image. We search for it in this matrix
# We find and filter it with numpy as :
threshold = 0.99  # Change this threshold so you get only 2 point in the array !
loc = np.where(res >= threshold)
print(loc)


w, h = template.shape[::-1]  # -1 gives col and row value in inverse order, ( width and height)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[0] + h), (0, 0, 255), 3)  # inPT, firstPoint is topLeft and last is buttomLeft


cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
