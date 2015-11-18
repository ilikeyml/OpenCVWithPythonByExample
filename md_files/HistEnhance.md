##清晰图像的制作##
清晰的图像是指能够清楚地反映被摄景物的明亮程度和细微的色彩差别的图像。对于难于体现亮度差别的图像，为使其清晰可见，采用增强对比度是简单而有效的方法。  
####增强对比度####
图像明亮部分与黑暗部分的亮度比称为对比度 (Contrast)  
对图像数据放大，可以得到增强图像的对比度  

<a href="http://www.codecogs.com/eqnedit.php?latex=g(x,y)&space;=&space;n&space;*&space;f(x,y)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?g(x,y)&space;=&space;n&space;*&space;f(x,y)" title="g(x,y) = n * f(x,y)" /></a>  

超出255范围的像素值，OpenCV会自动处理（Value - 256）  
更好的处理方式是使用直方图均衡化(Histogram Equlization)
要把浓度直方图均衡化，只需把原图像中像素少的部分进行压缩，而将像素较多的部分拉伸开来。  
下面，用一个简单的例子来说明平坦化的算法。先考虑浓度为0～7之处。平坦化后，各浓度像素值按照下面方式计算  
 
   <a href="http://www.codecogs.com/eqnedit.php?latex=Pixel&space;Num&space;For&space;Each&space;Grade&space;=&space;\frac{TotalPixels}{gradeNumCount}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Pixel&space;Num&space;For&space;Each&space;Grade&space;=&space;\frac{TotalPixels}{gradeNumCount}" title="Pixel Num For Each Grade = \frac{TotalPixels}{gradeNumCount}" /></a>   

一种像素浓度所分配的像素数 = 所有像素数目之和/像素浓度级数之和  
<table>
   <tr>
      <td>         浓度级</td>
      <td>7</td>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
   </tr>
   <tr>
      <td>原图像的各级的像素数</td>
      <td>0</td>
      <td>4</td>
      <td>9</td>
      <td>11</td>
      <td>5</td>
      <td>7</td>
      <td>4</td>
      <td>0</td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td>平坦化后的各级像素数</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
   </tr>
</table>

所有像素数目之和 = 0+4+9+11+5+7+4+0 = 40  
像素浓度级数之和 = 8  
平坦化后的各级像素 = 40/8 = 5  

####灰度图像的均衡化####
`img = cv.imread("..\ImageSource\Sample\couple.bmp", 0)`  
`print img.shape`  
`cv.imshow("in", img)`  
`out = cv.equalizeHist(img)`  
`cv.imshow("out", out)`   
*Origin*   
!["Histeq"](accessories\histEqgreyIn.png)  
*Histogram Equalization*  
!["Histeq"](accessories\histEqgreyOut.png)
####彩色图像的均衡化####
对于彩色图像，我们使用YUV空间，对V(亮度)分量进行输处理    
`#彩色图像对比度增强`  
`img_color = cv.imread("..\ImageSource\Sample\\airplane.bmp")`  
`print img_color.shape`  
`cv.imshow("img_color", img_color)`  
`img_colorYUV = cv.cvtColor(img_color, cv.COLOR_BGR2YUV)`  
`#对V亮度通道进行Histogram Equalization 处理`  
`img_colorYUV[:, :, 0] = cv.equalizeHist(img_colorYUV[:, :, 0])`  
`img_colorYUV_out = cv.cvtColor(img_colorYUV, cv.COLOR_YUV2BGR)`  
`cv.imshow("img_color_hist", img_colorYUV_out)`  

*Origin*   
!["Histeq"](accessories\histEqcolorIn.png)  
*Histogram Equalization*  
!["Histeq"](accessories\histEqcolorOut.png)