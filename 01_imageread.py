import cv2 as cv

# Загружаем изображение в переменную img:
img = cv.imread('datas/blue_car.jpg')

print(img.shape)
# В результате картинка будет показана неограниченное количество времени
# Визуализация изображения:
cv.imshow('blue_car', img)

# Указываем время демонстрации изображения на экране:
# Если в качестве аргумента установить 0, то картинка показана неограниченное количество времени
#cv.waitKey(0)

# Уснатановим время, равное 5 секундам:
cv.waitKey(3000)


