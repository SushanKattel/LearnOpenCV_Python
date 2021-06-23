import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread('road.jpg')
image = cv2.resize(image, (1279, 704))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
'''
Here, the lanes where vehicle travel is parallel which seems to merge at certain point. We can define our ROI here,
which is going to be a triangle.
'''
print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    (width, height)
]


# This func. masks everything other then ROI
'''  Read this function carefully hai 😊😊😊 '''
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  # Blank matrix that matches image height and width
    # channel_count = img.shape[2]  # Retriving no. of colour channels in the image
    #  # Since we are using greyscale image, we dont use channel_count here !
    #  match_mask_color = (255,) * channel_count  # create match colour with same colour channel count.
    match_mask_color = (255)  # only one channel so, only 255
    cv2.fillPoly(mask, vertices, match_mask_color)  # filling the polygon
    masked_image = cv2.bitwise_and(img, mask)  # Return only the image only where the masked pixel matches
    return masked_image


gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
cropped_image = region_of_interest(canny_image,
                                   np.array([region_of_interest_vertices], np.int32))

# cropped_image = region_of_interest(image,
#                                    np.array([region_of_interest_vertices], np.int32))
# #To find edges, we first convert our image to gray
# gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2GRAY)
# canny_image = cv2.Canny(gray_image, 100, 200)
# Finding this canny here gives other lines i.e., border lines too, so, we do this before finding ROI,
# i.e., we pass image instead of cropped_image

# Now, we draw lines on edges

lines = cv2.HoughLinesP(cropped_image,
                        rho=6, theta=np.pi / 60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40, maxLineGap=25)

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=4)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

image_with_lines = draw_the_lines(image, lines)

plt.imshow(image_with_lines)
plt.show()
