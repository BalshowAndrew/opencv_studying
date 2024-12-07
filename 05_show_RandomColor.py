import cv2 as cv
import os
os.environ["XDG_SESSION_TYPE"] = "xcb"


imgColor = cv.imread('datas/RandomColor.png')
cv.namedWindow("color", cv.WINDOW_AUTOSIZE)
while(1):
    cv.imshow("color", imgColor)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

