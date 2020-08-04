from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

def get_pic_byte(x, y, w, h):
    return ImageGrab.grab(bbox=(x, y, w, h))


def save_pic(x, y, w, h, path):
    pic = get_pic_byte(x, y, w, h)
    pic.save(path)


def get_pic(hwnd):
    app = QApplication(sys.argv)
    screen= QApplication.primaryScreen()#PyQt5
    img = screen.grabWindow(hwnd)
    img.save(r"D:\4.jpg")


if __name__ == "__main__":
    pic=get_pic_byte(0, 0, 200, 100)
    pic.save(r"D:\4.jpg")
