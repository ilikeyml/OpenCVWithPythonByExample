##Development Environment Configuration 开发环境配置##
**1.安装OpenCV**  
-通过 *OpenCV* 官网下载 *OpenCV* 源码以及编译文件，下载地址  [http://opencv.org/](http://opencv.org/ "opencv")   
!["OpenCV Download"](accessories/opencvdownload.png)   
选择合适的平台版本  
-文件下载完成，解压后在 *"..opencv\build\python\2.7"* 文件下找到合适的文件 *"(X86/X64)cv2.pyd"* *(windows platform)*

-将 *cv2.pyd* 文件拷贝到 *"..\Python27\Lib\site-packages"*   

-*OpenCV* 安装完成

*此时如果在python中调用  
`img = cv2.imread("ImageSource/scene.jpg")`  
`type(img)`  
输出的结果是 *<type 'numpy.ndarray'>*  
为了对 *"numpy.ndarray"* 数据类型进行处理，需要安装numpy  
**2.安装numpy**  
从下面链接下载Windows版本的numpy [numpy download](http://sourceforge.net/projects/numpy/files/NumPy/1.10.1/), 直接安装。  
安装完成后，在python中输入`import numpy` 测试安装是否成功  
以上， *OpenCV for Python* 安装完成
