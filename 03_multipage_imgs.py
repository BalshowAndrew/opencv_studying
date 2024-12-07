import cv2 as cv
import sys

success, grayImages = cv.imreadmulti(
    'datas/MyMultiPics.tiff',
    flags=cv.IMREAD_GRAYSCALE)

if not success:
    print('Failed to read images from file')
    sys.exit(1)

print ('Number of images:', len(grayImages))
success = cv.imwritemulti('datas/MyMultiPicsGray.tiff', grayImages)
if not success:
    print('Failed to write images to file')
    sys.exit(1)
