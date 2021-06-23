import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/asus/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

    cv2.imshow('IMG', img)
    if cv2.waitKey(40) == 27:   # esc to close
        break

cap.release()


