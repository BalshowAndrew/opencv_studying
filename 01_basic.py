import cv2 as cv
import numpy as np

# createng a 2D NumPy array:
img = np.zeros((5, 3), dtype=np.uint8)

print(img)
print(img.shape)

# convert image into blue-green-red format
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

print(img)
print(img.shape)




