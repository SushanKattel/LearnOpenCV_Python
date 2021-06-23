'''

It is the method used to calculate threshold for smaller region.
Here, the threshold is not global for every pixel.
If the lightning condition varies from point to point, we use adaptive thresholding.

'''

import cv2 as cv


img = cv.imread('standard_test_images/sudoku.jpg', 0)
img = cv.resize(img, (512, 512))
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) # 11 is block size: size of neigh. area
                                                                                    # 2 IS CONST. TO BE SUB. FROM MEAN
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


gray = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REPLICATE)
th4 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]

cv.imshow("image", img)
cv.imshow("Thresh Binary", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN", th3)
cv.imshow("Naya", th4)

cv.waitKey(0)
cv.destroyAllWindows()