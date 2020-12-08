import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('hazard10.jpg')
cv.imshow('BGR',img)
img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)


img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',img_hsv)
img_hsv_RGB = cv.cvtColor(img_hsv,cv.COLOR_BGR2RGB)

titles = ['original','hsv']
images = [img_RGB,img_hsv_RGB]

plt.axis("off")
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv.waitKey()
cv.destroyAllWindows()
