import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')
cv.imshow('BGR',img)
print('The shape of the image is')
print(img.shape)
print('The size of the image is')
print(img.size)

##img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
##cv.imshow('GRAY',img_gray)
##print('The shape of the image is')
##print(img_gray.shape)
##print('The size of the image is')
##print(img_gray.size)

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',img_hsv)
print('The shape of the image is')
print(img_hsv.shape)
print('The size of the image is')
print(img_hsv.size)

cv.waitKey()
cv.destroyAllWindows()
