import cv2 as cv
import numpy as np
import pytesseract as pyt

#taking iamge as input
from tkinter.filedialog import askopenfilename
filename=askopenfilename()

#reading image
image=cv.imread(filename)
image_work=np.copy(image)

#convertig to text and printing the output
text = pyt.image_to_string(image)
print(text)


cv.imshow('original',image)

cv.waitKey(0)
cv.destroyAllWindows()
