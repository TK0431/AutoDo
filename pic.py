from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys

def get_pic_byte(x, y, w, h):
    return ImageGrab.grab(bbox=(x, y, w, h))


def save_pic(x, y, w, h, path):
    pic = get_pic_byte(x, y, w, h)
    pic.save(path)

def get_pic(hwnd):
    app = QApplication(sys.argv)
    screen= QApplication.primaryScreen()#PyQt5
    img = screen.grabWindow(hwnd,0,0-1,-1).toImage()
    img.save(r"D:\4.jpg")
    return img

def get_pic2(pos):
    """
    left, top, right, bottom
    """
    l,t,r,b = pos
    print(l,t,r-l,b-t)
    app = QApplication(sys.argv)
    screen= QApplication.primaryScreen()#PyQt5
    img = screen.grabWindow(0,l,t,r-l,b-t).toImage()
    #(889, 251, 1799, 795)
    #img = screen.grabWindow(0,l,t,300,300).toImage()
    img.save(r"D:\4.jpg")
    return img
