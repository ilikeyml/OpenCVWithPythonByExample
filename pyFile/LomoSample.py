import cv2 as cv
import numpy as np
img = cv.imread("..\ImageSource\\flower.jpg")
r, c = img.shape[:2]
cv.imshow("in", img)
kernel_x = cv.getGaussianKernel(c, 200)
kernel_y = cv.getGaussianKernel(r, 200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel/np.linalg.norm(kernel)
out = np.copy(img)
for i in range(3):
    out[:, :, i] = out[:, :, i] * mask
cv.imshow("out", out)
print kernel_x.shape
cv.waitKey(0)