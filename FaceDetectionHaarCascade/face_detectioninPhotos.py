import cv2
# face_cascade = cv2.CascadeClassifier('trainedFiles/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('trainedFiles/haarcascade_frontalface_alt2.xml')
# Read the input image
img = cv2.imread("test2.jpg")
img = cv2.resize(img, (1024, 512))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
'''
objects = cv2.CascadeClassifier.detectMultiScale( image, scaleFactor, minNeighbors)
image = matrix of the type CV_8U containing an image where objects are detected.
objects = Vector of rectangles where each rectangle contains the detected object, the rectangles may be partially
          outside the original image.
scaleFactor = Parameter specifying how much the image size is reduced at each image scale.
minNeighbors = Parameter specifying how many neighbors each candidate rectangle have to retain it.
'''


for (x, y, w, h)in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)


cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


