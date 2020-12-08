import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('hazard10.jpg')
cv.imshow('Image',img)

##img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
##
##plt.axis('off')
##plt.imshow(img_RGB)
##plt.show()

ball = img[235:295,465:530]

##ball = ([255,255,255])
##img[235:295,465:530] = ball

img[235:295,555:620] = ball

cv.imshow('ROI',img)



cv.waitKey()
cv.destroyAllWindows()
