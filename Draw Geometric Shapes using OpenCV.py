import numpy as np
import cv2 as cv

img = np.zeros((512,512,3),np.uint8)

cv.line(img,(0,0),(511,511),(255,0,0),5)

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv.circle(img,(447,63),63,(0,0,255),-1)

pts = np.array([[100,50],[200,300],[70,200],[50,100]],np.int32)
cv.polylines(img,[pts],True,(0,255,255),3)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'mini project',(0,480),font,2,(255,255,255),2)

cv.imshow('Image',img)

cv.waitKey(0)
cv.destroyAllWindows()

