import cv2 as cv
import numpy as np

img = cv.imread("./Photos/lady.jpg")


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


# -x-->left
# /y-->up
# x-->right
# y-->down
cv.imshow("translated", translate(img, 100, 100))

# flipping images
flip = cv.flip(img, 1)
cv.imshow("flip", flip)
cv.waitKey(0)
