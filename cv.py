# coding=utf-8

# 导入python库
import cv2
import numpy as np
import matplotlib.pyplot as plt


def debug_show_img(img, title="debug"):
    """
    窗体显示图片
    """
    cv2.imshow(title, img)


def save_img(img, path):
    """
    图片保存
    """
    cv2.imwrite(path, img)

img = cv2.imread(r"D:\0.jpg")# 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# 彩色图片灰度化
edges = cv2.Canny(gray, 100, 200)# 执行边缘检测

debug_show_img(edges)
# plt.subplot(121)
# plt.imshow(edges)

# 执行Hough直线检测
lines = cv2.HoughLines(edges, 1, np.pi/180, 160)
lines1 = lines[:, 0, :]
for rho, theta in lines1:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

debug_show_img(img,"2")

cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.subplot(122)
# plt.imshow(img)
