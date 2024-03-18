# import cv2 as cv

# img = cv.imread("Photos\cat.jpg")
# cv.imshow('Cat', img)
# cv.waitKey(0)


#
# img = cv.imread("Photos\cat_large.jpg")
# cv.imshow("Cat", img)  # this image is too large and can't fit into the frame
# cv.waitKey(0)

# Reading Videos
# import cv2 as cv
# capture = cv.VideoCapture("Videos/dog.mp4")
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# import cv2 as cv
#
# capture = cv.VideoCapture("Videos/dog.mp4")
#
# if not capture.isOpened():
#     print("Error: Could not open video.")
#     exit()
#
# while True:
#     isTrue, frame = capture.read()
#
#     if not isTrue:
#         print("Error: Could not read frame.")
#         break
#
#     cv.imshow("Video", frame)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()
# import cv2 as cv
# img = cv.imread('Photos/cats.jpg')
# cv.imshow("cat", img)
# cv.waitKey(0)
#
# capture = cv.VideoCapture("Videos/dog.mp4")
#
# if not capture.isOpened():
#     print("Can't capture")
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Dog", frame)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
import cv2 as cv

img = cv.imread("./Photos/cat.jpg")
cv.imshow("Original_img", img)


def rescale_frame(frame, scale=0.75):
    # this method work for picture, images, Live Video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):
    # this is going to work just for live video
    capture.set(3, width)
    capture.set(4, height)


cv.imshow("resized", rescale_frame(img))
cv.waitKey(0)
capture = cv.VideoCapture("./Videos/dog.mp4")
if not capture.isOpened():
    print("Video Failed to open")
while True:
    isTrue, frame = capture.read()
    cv.imshow("resize_Video", rescale_frame(frame, scale=0.2))
    cv.imshow("Original", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
