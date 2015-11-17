##图像形状变化##
**1.图像大小变化**  
将某点 *(x,y)* 经扩大或缩小后，变化到 *(X,Y)* 所在的位置上。
   
<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{matrix}&space;X=S_x*x\\&space;Y=S_y*y&space;\end{matrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{matrix}&space;X=S_x*x\\&space;Y=S_y*y&space;\end{matrix}" title="\begin{matrix} X=S_x*x\\ Y=S_y*y \end{matrix}" /></a>  

变换矩阵  

<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;X\\&space;Y&space;\end{bmatrix}=\begin{bmatrix}&space;S_x&space;&0&space;\\&space;0&S_y&space;\end{bmatrix}\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;X\\&space;Y&space;\end{bmatrix}=\begin{bmatrix}&space;S_x&space;&0&space;\\&space;0&S_y&space;\end{bmatrix}\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}" title="\begin{bmatrix} X\\ Y \end{bmatrix}=\begin{bmatrix} S_x &0 \\ 0&S_y \end{bmatrix}\begin{bmatrix} x\\ y \end{bmatrix}" /></a> 

**2.位置的变化**  
像素平移 

<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{matrix}&space;X=x&plus;b_x\\Y=y&plus;b_y&space;\end{matrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{matrix}&space;X=x&plus;b_x\\Y=y&plus;b_y&space;\end{matrix}" title="\begin{matrix} X=x+b_x\\Y=y+b_y \end{matrix}" /></a>

变换矩阵  

<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;x'\\&space;y'&space;\end{bmatrix}=&space;\begin{bmatrix}&space;1&&space;0&space;\\&space;0&&space;1&space;\end{bmatrix}&space;\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}&plus;\begin{bmatrix}&space;b_x\\&space;b_y&space;\end{bmatrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;x'\\&space;y'&space;\end{bmatrix}=&space;\begin{bmatrix}&space;1&&space;0&space;\\&space;0&&space;1&space;\end{bmatrix}&space;\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}&plus;\begin{bmatrix}&space;b_x\\&space;b_y&space;\end{bmatrix}" title="\begin{bmatrix} x'\\ y' \end{bmatrix}= \begin{bmatrix} 1& 0 \\ 0& 1 \end{bmatrix} \begin{bmatrix} x\\ y \end{bmatrix}+\begin{bmatrix} x_0\\ y_0 \end{bmatrix}" /></a>

**3.图像的旋转**  
逆时针旋转θ角度的表达式  

<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{matrix}&space;X=x*cos\theta&space;&plus;&space;y*sin\theta&space;\\&space;Y=-x*sin\theta&space;&plus;&space;y*cos\theta&space;\end{matrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{matrix}&space;X=x*cos\theta&space;&plus;&space;y*sin\theta&space;\\&space;Y=-x*sin\theta&space;&plus;&space;y*cos\theta&space;\end{matrix}" title="\begin{matrix} X=x*cos\theta + y*sin\theta \\ Y=-x*sin\theta + y*cos\theta \end{matrix}" /></a>    

变换矩阵  

<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;X\\&space;Y&space;\end{bmatrix}=\begin{bmatrix}&space;cos\theta&space;&sin\theta&space;\\&space;-sin\theta&&space;cos\theta&space;\end{bmatrix}\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;X\\&space;Y&space;\end{bmatrix}=\begin{bmatrix}&space;cos\theta&space;&sin\theta&space;\\&space;-sin\theta&&space;cos\theta&space;\end{bmatrix}\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}" title="\begin{bmatrix} X\\ Y \end{bmatrix}=\begin{bmatrix} cos\theta &sin\theta \\ -sin\theta& cos\theta \end{bmatrix}\begin{bmatrix} x\\ y \end{bmatrix}" /></a>  

**4.齐次坐标**  

<a href="http://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;X\\Y&space;\\&space;1&space;\end{bmatrix}=\begin{bmatrix}&space;a_1_1&space;&a_1_2&space;&a_1_3&space;\\&space;a_2_1&space;&&space;a_2_2&space;&&space;a_2_3\\&space;0&space;&0&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;x\\y&space;\\&space;1&space;\end{bmatrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;X\\Y&space;\\&space;1&space;\end{bmatrix}=\begin{bmatrix}&space;a_1_1&space;&a_1_2&space;&a_1_3&space;\\&space;a_2_1&space;&&space;a_2_2&space;&&space;a_2_3\\&space;0&space;&0&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;x\\y&space;\\&space;1&space;\end{bmatrix}" title="\begin{bmatrix} X\\Y \\ 1 \end{bmatrix}=\begin{bmatrix} a_1_1 &a_1_2 &a_1_3 \\ a_2_1 & a_2_2 & a_2_3\\ 0 &0 & 1 \end{bmatrix}\begin{bmatrix} x\\y \\ 1 \end{bmatrix}" /></a>  

任何变换都可以由此齐次变换得到  

***Example***  
-图像缩放 
 
`# -*-coding:utf-8-*-`  
`import cv2 as cv`  
`import numpy as np`  
`img = cv.imread("../ImageSource/coffee.jpg")`  
`r, c = r, c = img.shape[:2]`  
`cv.imshow("in", img)` 
`#图像缩放`  
`img_scale = cv.resize(img, (180, 600), 1, 1, cv.INTER_LINEAR)`  
`cv.imshow("scale", img_scale)`  
`print img_scale.shape `    
!["Image Scale"](accessories/imageScale.png) 

-图像平移  

`transform_matrix = np.array([[1, 0, 70], [0, 1, 100]], np.float)`  
`print transform_matrix`  
`img_trans = cv.warpAffine(img, transform_matrix, (c, r))`  
`cv.imshow("img_trans", img_trans)`  
`cv.waitKey(0)`  

!["Image Shift"](accessories/imageShift.png)   

 
-图像旋转  

`rot_matrix = cv.getRotationMatrix2D((c/2, r/2), 30, 1)`  
`img_rot = cv.warpAffine(img, rot_matrix, (c, r))`  
`cv.imshow("img_rot", img_rot)`  

!["Image Rotation"](accessories/imageRotation.png)   

-投影变换  
`src_point = np.array([[0, 0], [c-1.0, 0], [0., r-1.0], [c-1.0, r-1.0]], np.float32)`  
`dst_point = np.array([[0, 0], [c-1.0, 0], [int(0.33*c), r-1], [int(0.66*c), r-1]], np.float32)`  
`projective_matrix = cv.getPerspectiveTransform(src_point, dst_point)`  
`img_out = cv.warpPerspective(img, projective_matrix, (c, r))`  
`cv.imshow("projective", img_out)`  
!["Image Projective"](accessories/imgProjective.png) 