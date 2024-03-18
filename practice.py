import cv2 as cv
import numpy as np

# img = cv.imread("./Photos/lady.jpg")
# cv.imshow("lady", img)
#
#
# def rescale_frame(frame, scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimension = (width, height)
#     return cv.resize(frame, dimension, interpolation=cv.INTER_LINEAR)
#
#
# capture = cv.VideoCapture(0)
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("vid", frame)
#     cv.imshow('cap', rescale_frame(frame))
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
#
# cv.imshow("image", rescale_frame(img))
# cv.waitKey(0)
blank = np.zeros((500, 500, 3), dtype="uint8")
blank[:] = 0, 255, 0

cv.imshow("blank", blank)
cv.waitKey(0)
