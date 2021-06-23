import cv2
face_cascade = cv2.CascadeClassifier('trainedFiles/ThirdTrainedFile.xml')
img = cv2.imread("test2.jpg")
img = cv2.resize(img, (1024, 512))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h)in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


