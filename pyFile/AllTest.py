import cv2 as cv
import numpy as np

img = cv.imread("..\ImageSource\Sample\crowd.tiff", 0)
print img.shape
cv.imshow("in", img)

cv.waitKey(0)