import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:/yantraDataset/TrainingDataSet/FlameGray/fg.5.jpg')
img = cv2.resize(img, (512, 512))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

canny = cv2.Canny(RGB, 9, 150)
cannyimg = canny.copy()

ret, thresh = cv2.threshold(cannyimg, 69, 200, 0)  # to imgGray
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))

cv2.drawContours(cannyimg, contours, -1, (255, 0, 255), 3) # to img

titles = ['image', 'Canny', 'Contour']
images = [RGB, canny, cannyimg]  # cannyimg to img
for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
