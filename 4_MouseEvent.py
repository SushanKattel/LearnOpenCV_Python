import cv2
import numpy as np

'''
To see all the events available inside cv2 lib. :
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
which results:
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 
'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN',
'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL',
'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

'''

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(img, strXY, (x,y), font,.5, (0, 0, 255), 0, cv2.LINE_AA)
        cv2.imshow('image', img)

        points.append((x,y))
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (255,0,0),5)  # -1 gives last point, -2 gives sec.last point
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        strBGR = str(blue) + ',' + str(green)+ ',' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 0, cv2.LINE_AA)
        cv2.imshow('image', img)
        # Gives BGR value of colour of clicked place
        # open certain image to test

        # mycolorimage = np.zeros((512, 512, 3), np.uint8)
        # mycolorimage[:] = [blue, green, red]
        # cv2.imshow('clickedcolor', mycolorimage)
        # This will show next window filled with clicked color


points = []
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
