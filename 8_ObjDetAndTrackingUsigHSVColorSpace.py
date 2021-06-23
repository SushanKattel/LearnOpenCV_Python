'''

HSV - Hue, Saturation and Value
-> Hue corresponds to the color components(base Pigment), hence just by selecting a range of Hue,
We can select any color. (0-360)
-> Saturation is the amount of color (Depth of the pigment) (Dominance of Hue) (0-100%)
-> Value is basically the brightness of the color. (0-100%)
This comes to use when we need illumenance to our image

'''

import cv2
import numpy as np
def nothing(x):
    pass

#cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while True:
    frame = cv2.imread('standard_test_images/ballsJPG.jpg')
    #_, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # l_b = np.array([110, 50, 50])
    # u_b = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(1) &0xFF
    if k == 27:  #ESC key
        break

#cap.release()
cv2.destroyAllWindows()


'''
To do this for video:
add:
cap = cv2.VideoCapture(0)
before tracking 
and, in while loop:

_, frame = cap.read()
by commenting imread, which is going to read the frames from default camera.
and at last, 
cap.release()
to release all the resources.

'''

