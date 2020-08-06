from help_user32 import *
from pic import *
from help_cv import *
from key import *
import _thread


def press_a():
    send_key_sed('a', 0.1)


def press_w():
    send_key_sed('w', 0.1)


def press_s():
    send_key_sed('s', 0.1)


def press_d():
    send_key_sed('d', 0.1)


hwnd = get_hwnd("逍遥模拟器", "Qt5QWindowIcon")
path = r"D:\12.jpg"

set_top_hwnd(hwnd)

flg = True
while True:
    try:
        # 窗口截图
        read_hwnd_save_img(hwnd, path)
        # 截图保存
        img = read_img(path)
        # debug_show_img(img)
        #img = None
        if flg:
            _thread.start_new_thread(press_a)
            _thread.start_new_thread(press_w)
            flg = False
    except Exception as e:
        print(e)
    # time.sleep(100)
    cv2.waitKey(1)
