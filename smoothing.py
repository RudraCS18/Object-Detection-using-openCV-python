import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

##img = cv.imread('opencv-logo.png')

##img = cv.imread('ellipses.jpg')

img = cv.imread('lena.jpg')

##blur = cv.blur(img,(5,5))

gauss_blur = cv.GaussianBlur(img,(5,5),0)

##median = cv.medianBlur(img,5)

bilateral = cv.bilateralFilter(img,9,75,75)

plt.subplot(131)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(gauss_blur)
plt.title('Gaussian Blur')
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(bilateral)
plt.title('Bilateral Filter')
plt.xticks([])
plt.yticks([])

plt.show()

