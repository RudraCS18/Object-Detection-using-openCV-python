import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img =  cv.imread('hazard10.jpg')
cv.imshow('BGR',img)

img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img_RGB)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

