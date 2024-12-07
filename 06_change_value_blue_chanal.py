import cv2 as cv

img = cv.imread('datas/MyPic.png')
print(img.item(150, 120, 0))

img[150, 120, 0] = 255

print(img.item(150, 120, 0))
