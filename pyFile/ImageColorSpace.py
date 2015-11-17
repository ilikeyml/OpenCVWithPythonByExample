# -*-coding:utf-8-*-
'''
将图像分通道处理以及图像空间转换
'''
import cv2 as cv
img = cv.imread("../ImageSource/redSample.jpg")
cv.imshow("in", img)
print img.shape
B, G, R = cv.split(img)
cv.imshow("B channel", B)
cv.imshow("G channel", G)
cv.imshow("R channel", R)
cv.waitKey(0)