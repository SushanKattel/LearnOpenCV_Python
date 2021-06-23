import cv2
import numpy as np

img = cv2.imread('standard_test_images/BasicShapes.jpg')
imgo = img.copy()
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)

contours, _ =  cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    # Epsilon 0.01 is accuracy, cv2.arcL.. calculates curve length (contour param., and true is for closed contur, in both cases here.
    cv2.drawContours(img, [approx], 0, (0,255,255), 5) # We take 1 contour at a time so, 0.
    x = approx.ravel()[0] + 5
    y = approx.ravel()[1] - 9
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,100,255))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:  # Ideally it is 1 but for noise, we have these
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (150,99,250))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))

cv2.imshow("original", imgo)
cv2.imshow("Processed", img)
#cv2.imshow("originalGrey", imgGrey)
cv2.waitKey(0)
cv2.destroyAllWindows()