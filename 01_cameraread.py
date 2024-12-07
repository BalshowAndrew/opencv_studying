import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)

while True:
    success, img = cap.read()
    cv.imshow('camera', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
