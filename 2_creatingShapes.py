import cv2

#  import numpy as kattel

#  abc=kattel.zeros((512,512,3),kattel.uint8) #512 512 is height and width, 3 is no. of colors:RGB uint is unsigned int and 8 is hexadecimal.

import numpy as np
abc = np.zeros((512, 512, 3), np.uint8)

'''
x1,y1 -------
|            |
|            |
|            |
---------x2,y2

'''

# cv2.rectangle(abc,(440,0),(505,300),(161,67,135),3)
cv2.rectangle(abc, (200, 300), (300, 200), (255, 125, 99), 2)
cv2.circle(abc, (100, 100), 33, (125, 33, 99), -3)  # - fills the shape.
cv2.line(abc, (400, 400), (500, 500), (0, 0, 255), 3) # NameofFrame, start, End, BGRvalues, Thickness

text1 = "Sushan Kattel"
cv2.putText(abc, text1, (130, 180), cv2.FONT_HERSHEY_TRIPLEX, 1, (123, 99, 33))

text2 = "Yeah !!"
cv2.putText(abc, text2, (100, 380), cv2.FONT_HERSHEY_COMPLEX, 3, (123, 123, 255))

cv2.imshow("Sushan", abc)
cv2.waitKey(0)
cv2.destroyAllWindows()

