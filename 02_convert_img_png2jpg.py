import cv2 as cv
import sys

image = cv.imread('datas/MyPic.png')

if image is None:
    print('Failed to read image from file')
    sys.exit(1)

success = cv.imwrite('datas/MyPic.jpg', image)

if not success:
    print('Filed to write image to file')
    sys.exit

grayImage = cv.imread('datas/MyPic.png', cv.IMREAD_GRAYSCALE)
if grayImage is None:
    print('Failed to read image from file')
    sys.exit(1)

success = cv.imwrite('datas/MyPicGray.png', grayImage)
if not success:
    print('Failed to write image to file')
    sys.exit(1)
