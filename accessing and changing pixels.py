import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')
cv.imshow('image',img)

print('The shape of the Image is')
print(img.shape)

print('The size of the Image is')
print(img.size)

print('The Datatype of the pixel values in the image is')
print(img.dtype)

px = img[100,100]
print('the value of the pixel at 100x100 is')
print(px)

blue = img[100,100,0]
print('the value of the blue color in pixel at 100x100 is')
print(blue)

img[100,100] = [255,255,255]
cv.imshow('image1',img)



cv.waitKey(0)
cv.destroyAllWindows()
