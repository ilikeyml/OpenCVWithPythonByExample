# -*-coding:utf-8-*-
import cv2 as cv
import numpy as np
img = cv.imread("../ImageSource/coffee.jpg")
r, c = img.shape[:2]
print img.shape
cv.imshow("in", img)
'''
#图像缩放
img_scale = cv.resize(img, (180, 600), 1, 1, cv.INTER_LINEAR)
cv.imshow("scale", img_scale)
print img_scale.shape
'''
#图像平移
'''
transform_matrix = np.array([[1, 0, 70], [0, 1, 110]], np.float)
print transform_matrix
img_trans = cv.warpAffine(img, transform_matrix, (c, r))
img_trans = cv.warpAffine(img, transform_matrix, (c+70, r+110))
cv.imshow("img_trans", img_trans)
transform_matrix2 = np.array([[1, 0, -30], [0, 1, -50]], np.float)
img_trans2 = cv.warpAffine(img_trans, transform_matrix2, (c+70+30, r+110+50))
cv.imshow("img_trans_2", img_trans2)
'''
#图像旋转
'''
rot_matrix = cv.getRotationMatrix2D((c/2, r/2), 30, 1)
img_rot = cv.warpAffine(img, rot_matrix, (c, r))
cv.imshow("img_rot", img_rot)
'''
#投影变换
src_point = np.array([[0, 0], [c-1.0, 0], [0., r-1.0], [c-1.0, r-1.0]], np.float32)
dst_point = np.array([[0, 0], [c-1.0, 0], [int(0.33*c), r-1], [int(0.66*c), r-1]], np.float32)
projective_matrix = cv.getPerspectiveTransform(src_point, dst_point)
img_out = cv.warpPerspective(img, projective_matrix, (c, r))
cv.imshow("projective", img_out)
cv.waitKey(0)