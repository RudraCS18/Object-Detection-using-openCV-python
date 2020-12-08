import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')

##res = cv.resize(img, (400,300), 0, 0, interpolation = cv.INTER_LINEAR)

res = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)

cv.imshow('original',img)
cv.imshow('scaled',res)

cv.waitKey()
cv.destroyAllWindows()

print('shape of original image')
print(img.shape)
print('shape of resized image')
print(res.shape)
