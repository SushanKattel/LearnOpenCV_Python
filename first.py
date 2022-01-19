import cv2
import numpy as np

img = cv2.imread("F:/personal files/photos/birthday 076 photos/IMG_20200317_224019.jpg", 0 ) # Give location to your image
#1 for color image, 0 for grayscale, -1 for loading image as such including alpha channel
print(img)

# cv2.imshow("Image", img)
# cv2.waitKey(0)

#cv2.imwrite("newname.extension", image to copy)

'''
np.savetxt("myfile.txt",img)

y = np.loadtxt("myfile.txt", delimiter=" ")
print(y)
'''
# Video

cap = cv2.VideoCapture(0)  # If 0 doesn't work, use -1. For multiple cams., try 1 for first cam, 2 for sec. ..
#cap = cv2.VideoCapture("name.avi")  # to open the vid file

'''
To save the vid file:

fourcc = cv2.VideoWriter_fourcc(*'XVID') # Get more about fourcc codes on their websites.
cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480) )  # 20.0 is fps. (640, 480) is size of vid file.

Now, on while (cap.isOpened()) or while (True) loop, add this:
if ret == True:
    out.write(frame)
else:
    break
    
and, at last, add: out.release()

'''



#while (cap.isOpened()): # You can use this too 😊 Cause, if device or file is opened, this func. will be true
# Try printing this: print(cap.isOpened())
while (True):
    ret, frame = cap.read() # ret will return true if frame is available and saved to frame variable.

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("framename", gray)  # These 2 lines will show grayscale vid.

    # To read height and width of frame:
    # cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #Print it
    # cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    #See documentation for cap. to get more 😊😊

    cv2.imshow("framename", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # the 0xFF mask is for 64 bit machines
        break

cap.release()
cv2.destroyAllWindows()
