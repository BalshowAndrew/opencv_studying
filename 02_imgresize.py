import cv2 as cv

img = cv.imread('datas/blue_car.jpg')

print(img.shape)

# Измерим размер картинки:

img_01 = cv.resize(img, (500, 300))

print(img_01.shape)

# Пропорциональное изменение размеров картинки
img_02 = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3))
print(img_02.shape)

# Выведем карнитку на экран:
cv.imshow('img_02', img_02[100:500, 200:1000])
cv.waitKey(3000)
