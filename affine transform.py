import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('hazard10.jpg')

pts1 = np.float32([[100,100],[100,200],[200,100]])

cv.line(img,(pts1[0,0],pts1[0,1]),(pts1[1,0],pts1[1,1]),(255,0,0),2)
cv.line(img,(pts1[1,0],pts1[1,1]),(pts1[2,0],pts1[2,1]),(0,255,0),2)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Input')

plt.show()
