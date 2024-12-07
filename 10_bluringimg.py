import cv2 as cv
import numpy as np

# Уменьшим исходное изображение и сохраним его под новым именем
img = cv.imread('datas/blue_car.jpg')

img = cv.resize(img, (img.shape[1] // 10, img.shape[0] // 10))
success = cv.imwrite('datas/car.jpg', img)
print(success)

# Применим Гаусово размытие для нового изображения
img = cv.imread('datas/car.jpg')
bimg = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)

cv.imshow('Result', np.hstack((img, bimg)))
cv.waitKey(0)
cv.destroyAllWindows()



