# -*-coding:utf-8-*-
import cv2 as cv
import numpy as np
'''
img = cv.imread("..\ImageSource\Sample\lena_color.tiff", 0)
cv.imshow("in", img)
cv.imwrite("..\\accessories\lena.png", img)
kernel_3x3 = np.ones((3, 3), np.float)/9.0
img_out = cv.filter2D(img, -1, kernel_3x3)
cv.imshow("Blur_3x3", img_out)
cv.imwrite("..\\accessories\lena_3x3.png", img)
img_blur = cv.blur(img, (3, 3))
cv.imshow("Img_Blur", img_blur)
cv.imwrite("..\\accessories\lena_blur.png", img)
img_sub = cv.subtract(img_out, img)
cv.imshow("Img_Sub", img_sub)
'''
'''
img = cv.imread("..\ImageSource\shape.png", 0)
cv.imshow("in", img)
sobel_H = cv.Sobel(img, cv.CV_64F, 1, 0)
sobel_V = cv.Sobel(img, cv.CV_64F, 0, 1)
cv.imshow("H", sobel_H)
cv.imshow("V", sobel_V)
laplacian_img = cv.Laplacian(img, cv.CV_64F)
cv.imshow("Laplacian", laplacian_img)
'''
'''
#Laplacian
img = cv.imread("..\ImageSource\Sample\lax.tiff", 0)
cv.imshow("in", img)
laplacian_img = cv.Laplacian(img, cv.CV_64F)
cv.imshow("Laplacian", laplacian_img)
canny = cv.Canny(img, 50, 240)
cv.imshow("Canny", canny)
'''
img = cv.imread("..\ImageSource\Sample\\airplane.bmp")
cv.imshow("in", img)
size = 50
motion_kernel = np.zeros((size, size))
motion_kernel[int((size-1)/2), :] = np.ones(size)
motion_kernel = motion_kernel/size
img_out = cv.filter2D(img, -1, motion_kernel)
cv.imshow("out", img_out)
cv.waitKey(0)
