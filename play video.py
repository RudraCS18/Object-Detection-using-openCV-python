import cv2 as cv
import numpy as np

vid = cv.VideoCapture('vtest.avi')

while(vid.isOpened()):
    ret, frame = vid.read()

    cv.imshow('frame',frame)

    key = cv.waitKey(20)
    if key == 27:
        break
vid.release()
cv.destroyAllWindows()
