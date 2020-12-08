import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while(True):
    ret, frame = cam.read()

    cv.imshow('frame',frame)
    key = cv.waitKey(10)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()
