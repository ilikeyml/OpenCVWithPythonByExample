# -*-coding:utf-8-*-
'''
实现图像读取、显示、图像保存
'''
import cv2 as cv
img = cv.imread("../ImageSource/coffee.jpg")
winName = "ImageShow"
cv.imshow(winName, img)
cv.imwrite("new_coffee.jpg", img)
cv.waitKey(0)
