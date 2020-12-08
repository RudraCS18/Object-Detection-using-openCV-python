import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')
cv.imshow('BGR',img)

##b,g,r = cv.split(img)
##cv.imshow('Blue',b)
##cv.imshow('Green',g)
##cv.imshow('Red',r)
##
##img_merge_bgr = cv.merge([b,g,r])
##cv.imshow('Merge_BGR',img_merge_bgr)

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',img_hsv)

h,s,v = cv.split(img_hsv)
cv.imshow('Hue',h)
cv.imshow('Saturation',s)
cv.imshow('Value',v)

img_merge_hsv = cv.merge([h,s,v])
cv.imshow('Merge_HSV',img_merge_hsv)


cv.waitKey(0)
cv.destroyAllWindows()
