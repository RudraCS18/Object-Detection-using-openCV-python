import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')

rows = img.shape[0]
cols = img.shape[1]

M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,0.5)

dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('Original',img)
cv.imshow('Rotated',dst)

cv.waitKey(0)
cv.destroyAllWindows()
