import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('hazard10.jpg')

pts1 = np.float32([[165,200],[800,200],[830,350],[135,350]])
pts2 = np.float32([[50,50],[775,50],[775,250],[50,250]])

M = cv.getPerspectiveTransform(pts1,pts2)

dst = cv.warpPerspective(img, M, (800,300))

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Input')

plt.subplot(1,2,2)
plt.imshow(dst)
plt.title('output')

plt.show()
