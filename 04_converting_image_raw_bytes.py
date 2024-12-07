import cv2 as cv
import numpy as np
import os
os.environ["XDG_SESSION_TYPE"] = "xcb"

# Make an array of 120,00 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

print(flatNumpyArray.shape)

# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv.imwrite('datas/RandomGray.png', grayImage)

print(grayImage.shape)

imgGray = cv.imread('datas/RandomGray.png', cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
while(1):
    cv.imshow("main", imgGray)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv.imwrite('datas/RandomColor.png', bgrImage)

print(bgrImage.shape)

