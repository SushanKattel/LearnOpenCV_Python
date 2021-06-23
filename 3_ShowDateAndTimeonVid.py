import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 1280)  # Arg 3 is new width
cap.set(4, 720)   # Arg 3 is new height. Remember: This can only be camera's supported resoluton ! But, wouldn't give error
print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        text = 'Width: '+ str(cap.get(3))+'  Height: '+ str(cap.get(4)) # Conv. int to str and concatinating!
        frame = cv2.putText(frame, text, (3, 33), font, 1, (0, 0, 255), 0, cv2.LINE_AA) # 1 is font size, 0 is thickness

        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (3, 90), font, 1, (0, 0, 255), 0, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) &0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()