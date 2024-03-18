import cv2 as cv
# import numpy as np
# blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("blank", blank)
#
# blank[200:300, 300:400] = 0, 0, 255
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), color=(0, 255, 0), thickness=-1)
# cv.circle(blank, center=(255, 255), radius=50, color=(0, 0, 255), thickness=-2)
# cv.line(blank, (0, 0), (255, 255), color=(255, 255, 255), thickness=3)
# cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX,1.0, color=(0, 255, 0), thickness=2)
# cv.imshow("Colourful_img", blank)
# cv.waitKey(0)
img = cv.imread('./Photos/group 1.jpg')
cv.imshow("Original", img)
# BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
# Bluring the images
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)
canny = cv.Canny(blur, 125, 175)
# edge detection
cv.imshow("canny", canny)
# dilate the canny images
dilate = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow("dilate", dilate)
# eroding the dilate image
eroded = cv.erode(dilate, (3, 3), iterations=1)
cv.imshow("eroded", eroded)
# resizing the images
resized = cv.resize(img, (500, 500), cv.INTER_CUBIC)
cv.imshow("Resized", resized)
# Croping Images
crop = img[50:200, 200:400]
cv.imshow("Crop", crop)
cv.waitKey(0)
