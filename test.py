from help_user32 import *
from pic import *
from help_cv import *
from key import *
from logic import *


def press_a():
    send_key_sed('a', 0.1)


def press_w():
    send_key_sed('w', 0.1)


def press_s():
    send_key_sed('s', 0.1)


def press_d():
    send_key_sed('d', 0.1)


hwnd = get_hwnd("AutoTest", None)
path = r"D:\12.jpg"

set_top_hwnd(hwnd)

flg = True
while True:
    try:
        top_hwnd = get_top_hwnd()
        #if top_hwnd != hwnd:
            

        # 窗口截图
        read_hwnd_save_img(hwnd, path)
        # 截图保存
        img = read_img(path)
        debug_show_img(img)
        #img = None

        pic_start(img)

        #time.sleep(0.1)
        cv2.waitKey(100)
    except Exception as e:
        print(e)
        break