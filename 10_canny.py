import cv2 as cv
import numpy as np

kernel = np.ones((3, 3), np.uint8)

img = cv.imread('datas/car_gray.jpg')

img = cv.Canny(img, 100, 100)

# Увеличим жирность линий
img = cv.dilate(img, kernel, iterations=1)

# Уменьшим жирность линий
img = cv.erode(img, kernel, iterations=1)

cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()
