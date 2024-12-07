import cv2 as cv

cap = cv.VideoCapture('datas/traffic.mp4')

while True:
    success, img = cap.read()
    cv.imshow('traffic', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
