import cv2 as cv
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

cv.rectangle(photo, (80, 80),(100, 100), (119, 201, 105), thickness=3)

cv.imshow('Result', photo)
cv.waitKey(0)
cv.destroyAllWindows()
