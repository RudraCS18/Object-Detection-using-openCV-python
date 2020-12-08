import cv2 as cv
import numpy as np

cam = cv.VideoCapture()

fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('Output.avi',fourcc,20.0,(640,480))

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret == True:
        cv.imshow('frame',frame)
        output.write(frame)

        if cv.waitKey(1) == ord('q'):
            print('saved video')
            break
        else:
            print('Error in capturing video')
            break

cam.release()
output.release()
cv.destroyAllWindows()
