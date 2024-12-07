import cv2 as cv

cameraCaptuer = cv.VideoCapture(0)
fps = 30
size = (int(cameraCaptuer.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cameraCaptuer.get(cv.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv.VideoWriter(
    'MyOutputVid.avi',
    cv.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)
success, frame = cameraCaptuer.read()
numFrameRemaining = 10 * fps - 1
while success and numFrameRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCaptuer.read()
    numFrameRemaining -= 1
