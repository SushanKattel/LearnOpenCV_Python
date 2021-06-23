import cv2

imga = cv2.imread("standard_test_images/mandril_colorJPG.jpg")
imga = cv2.resize(imga, (512, 512))

print(imga.shape) # Returns a tuple of no. of rows, columns, and channels
print(imga.size) # Returns total no. of pixels is accessed
print(imga.dtype) # Returns image datatype is obtained

b,g,r = cv2.split(imga)
imga = cv2.merge((b,g,r))

cv2.imshow('image', imga)

imgb = cv2.imread("standard_test_images/a_greyscale.jpg")
imgb = cv2.resize(imgb, (512, 512))

dsta = cv2.add(imga, imgb)
cv2.imshow('imagea', dsta)

dstb = cv2.addWeighted(imga, 0.3, imgb, 0.7, 0)
cv2.imshow('imageb', dstb)


cv2.waitKey(0)
cv2.destroyAllWindows()

'''
ROI stands for region of interest. Sometimes, we have to work with only certain region of images like face
or, only ball, or only eyes, etc., which are called region of interest.
Like, I want to work with eye which is my ROI and I want to copy it to new location.
use this to get the co-ordinates of ROI:


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(imga, strXY, (x,y), font,.5, (0, 0, 255), 0, cv2.LINE_AA)
        cv2.imshow('image', imga)

cv2.imshow('image', imga)
cv2.setMouseCallback('image', click_event)

# and remove cv2.imshow of above waitkey.


eyeO = imga[156:56, 190:71]
imga[153:211, 180:233] = eyeO

check for this once:  #vid 10 contd.
'''

