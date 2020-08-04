# coding=utf-8

# 导入python库
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('test3.jpg') 
# 彩色图片灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 执行边缘检测
edges = cv2.Canny(gray,100,200)
# 显示原始结果

cv2.imwrite('edges.png',edges)
cv2.imshow('edge', edges)
# plt.subplot(121)
# plt.imshow(edges)

# 执行Hough直线检测
lines = cv2.HoughLines(edges,1,np.pi/180,160)
lines1 = lines[:,0,:]
for rho,theta in lines1:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a)) 
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

cv2.imwrite('line.png',img)
cv2.imshow('line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.subplot(122)
# plt.imshow(img)