import cv2 as cv
import os
os.environ["XDG_SESSION_TYPE"] = "xcb"

img = cv.imread('datas/MyPic.jpg')
my_roi = img[0:50]
img[50:100] = my_roi

cv.namedWindow("color", cv.WINDOW_AUTOSIZE)
while(1):
    cv.imshow("color", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

