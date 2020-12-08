import cv2 as cv
import numpy as np

img = cv.imread('pic1.png')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray,127,255,0)

contours, hierachy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0,255,0),3)

cv.imshow('Contours',img)

cv.waitKey(0)
cv.destroyAllWindows()

