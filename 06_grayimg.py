import cv2 as cv

img = cv.imread('datas/car.jpg')

grimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite('datas/car_gray.jpg', grimg)

cv.imshow('Result', grimg)
cv.waitKey(0)
cv.destroyAllWindows()

