import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("standard_test_images/BWa.jpg")


bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
# Try for bitwise_xor and bitwise_not 'bitwise_not takes only one img.'
'''
    AND            OR              XOR
0  0  -> 0     0   0  -> 0     0   0  -> 0
0  1  -> 0     0   1  -> 1     0   1  -> 1
1  0  -> 0     1   0  -> 1     1   0  -> 1
1  1  -> 1     1   1  -> 1     1   1  -> 0

'''

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)

cv2.waitKey(0)
cv2.destroyAllWindows()