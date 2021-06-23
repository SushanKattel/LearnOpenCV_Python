import cv2
import numpy as np

apple = cv2.imread('standard_test_images/appleA.jpg')
orange = cv2.imread('standard_test_images/orangeA.jpg')

# Now, lets blend half apple with half orange:
# First, let's try by cutting and joining !
apple_orange1 = np.hstack((apple[:,:256], orange[:, 256:]))
# we see sharp line in mid. so we use pyramids to blend.
'''

We need to follow following 5 steps to blend images using pyramids.
1. Load the two images of apple and orange.
2. Find the gaussian pyramids for apple and orange (Here, number of levels is 6
3. From Gaussian pyramids, find their Laplacian pyramids.
4. Now join the left half of apple and right half of orange in each levels of laplacian pyramids.
5. Finally from this joint image pyramids, reconstruct the original image.

'''
# Generate Gaus. Pyr for apple -step 2
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Generate Gaus. Pyr for orange -step 2
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Generate Lap. Pyr. for apple: -step 3
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)


# Generate Lap. Pyr. for orange: -step 3
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)

# Now add left and right halves of images in each level: -step 4
apple_orange2 = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    #laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):0]))
    apple_orange2.append(laplacian)

# Now, reconstruct - step 5

apple_orange_reconstruct = apple_orange2[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange2[i], apple_orange_reconstruct)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)

cv2.imshow("apple_orange1", apple_orange1)

cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()

