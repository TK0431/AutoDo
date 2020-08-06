from help_user32 import *
from pic import *
from help_cv import *
import time
import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *


hwnd = get_hwnd(None,"Notepad")
#hwnd = get_hwnd("AutoTest",None)
#hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
while True:
    try:
        img = read_hwnd0_img(hwnd)
        #img = get_pic2(get_win_rect(hwnd))
        debug_show_img(read_qt5_img(img))
        #img = None
    except Exception as e:
        print(e)
    #time.sleep(100)
    cv2.waitKey(1)