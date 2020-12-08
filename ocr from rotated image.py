import cv2 as cv
import numpy as np
import pytesseract as pyt

from tkinter.filedialog import askopenfilename
filename = askopenfilename()

image = cv.imread(filename)
image_work = np.copy(image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
gray = cv.bitwise_not(gray)

ret,thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY)

cv.imshow('Thresholded',thresh)
cv.waitKey(1000)

coords = np.column_stack(np.where(thresh > 0))
rect = cv.minAreaRect(coords)
angle = cv.minAreaRect(coords)[-1]

if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

print("angle is : {:.3f}".format(angle)+"degrees")

(h, w) = image.shape[:2]
center = (w//2, h//2)

M = cv.getRotationMatrix2D(center, angle, 1.0)
rotated = cv.warpAffine(image, M, (w,h),
                        flags=cv.INTER_CUBIC,
                        borderMode=cv.BORDER_REPLICATE)

cv.imshow("Rotated",rotated)

cv.waitKey(0)
cv.destroyAllWindows()

text = pyt.image_to_string(rotated)

print(text)



