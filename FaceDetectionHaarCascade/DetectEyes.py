import cv2
import imutils


class EyeTracker:
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

    def track(self, image):
        faceRects = self.faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=9,
                                                      minSize=(30, 30))
        rects = []
        for (fX, fY, fW, fH) in faceRects:
            faceROI = image[fY:fY + fH, fX:fX + fW]
            rects.append((fX, fY, fX + fW, fY + fH))
            eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor=1.1, minNeighbors=10,
                                                        minSize=(15, 15))

            for (eX, eY, eW, eH) in eyeRects:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))

        return rects


face = "E:/programProjects/ProjectLearnOpencv/FaceDetectionHaarCascade/trainedFiles/haarcascade_frontalface_default.xml"
eye = "E:/programProjects/ProjectLearnOpencv/FaceDetectionHaarCascade/trainedFiles/haarcascade_eye.xml "
et = EyeTracker(face, eye)
camera = cv2.VideoCapture(0)
while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    frame = imutils.resize(frame, width=900)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = et.track(gray)

    for rect in rects:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (255, 255, 0), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()