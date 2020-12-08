import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')

rows = img.shape[0]
cols = img.shape[1]

M = np.float32([[1,0,100],[0,1,50]])

dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('Original',img)
cv.imshow('Translated',dst)

cv.waitKey()
cv.destroyAllWindows()
