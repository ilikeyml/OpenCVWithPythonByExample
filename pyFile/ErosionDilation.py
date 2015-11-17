import cv2 as cv
import numpy as np
img = cv.imread("..\ImageSource\sign.png", 0)
cv.imshow("in", img)
print img.shape
kernel = np.ones((7, 7), np.uint8)
img_ero = cv.erode(img, kernel, iterations=1)
img_dila = cv.dilate(img, kernel, iterations=1)
cv.imshow("Erosion", img_ero)
cv.imshow("Dilation", img_dila)
cv.imwrite("..\ImageSource\sign_dila.png", img_dila)
cv.imwrite("..\ImageSource\sign_ero.png", img_ero)
cv.waitKey(0)