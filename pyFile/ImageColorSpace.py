# -*-coding:utf-8-*-
'''
将图像分通道处理以及图像空间转换
'''
import cv2 as cv
img = cv.imread("../ImageSource/redSample.jpg")
cv.imshow("in", img)
print img.shape
'''
B, G, R = cv.split(img)
cv.imshow("B channel", B)
cv.imshow("G channel", G)
cv.imshow("R channel", R)
'''
#BGR2YUV 转换
img_YUVtrans = cv.cvtColor(img,cv.COLOR_BGR2YUV)
cv.imshow("YUV mode", img_YUVtrans)
#BGR2HSV 转换
img_HSVtrans = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV mode", img_HSVtrans)
cv.waitKey(0)