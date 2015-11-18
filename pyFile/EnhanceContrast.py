# -*-coding:utf-8-*-
import cv2 as cv
'''
img = cv.imread("..\ImageSource\Sample\couple.bmp", 0)
print img.shape
cv.imshow("in", img)
out = cv.equalizeHist(img)
cv.imshow("out", out)
'''
#彩色图像对比度增强
img_color = cv.imread("..\ImageSource\Sample\\airplane.bmp")
print img_color.shape
cv.imshow("img_color", img_color)
img_colorYUV = cv.cvtColor(img_color, cv.COLOR_BGR2YUV)
#对V亮度通道进行Histogram Equalization 处理
img_colorYUV[:, :, 0] = cv.equalizeHist(img_colorYUV[:, :, 0])
img_colorYUV_out = cv.cvtColor(img_colorYUV, cv.COLOR_YUV2BGR)
cv.imshow("img_color_hist", img_colorYUV_out)

cv.waitKey(0)