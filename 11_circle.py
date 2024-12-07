import cv2 as cv
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

cv.rectangle(photo, (80, 80),(100, 100), (119, 201, 105), thickness=3)

# Добавим горизонтальную линию, которая делит изображение пополам
cv.line(photo, (0, photo.shape[0]//2), (photo.shape[1], photo.shape[0]//2), (119, 201, 105), thickness=5)

# Добавим круг с центром в середине изображения
cv.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 50, (119, 210, 105), thickness=cv.FILLED)

cv.imshow('Result', photo)
cv.waitKey(0)
cv.destroyAllWindows()

