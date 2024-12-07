import cv2 as cv
# import numpy as np

img = cv.imread('datas/MyPic.png')
cv.imshow('my img', img)
cv.waitKey()
cv.destroyAllWindows()

