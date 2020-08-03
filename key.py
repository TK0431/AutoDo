from pymouse import *      # 模拟鼠标所使用的包
from pykeyboard import *   # 模拟键盘所使用的包
import time                # 连续进行两个动作可能太快而效果不明显，因此加入暂停时间

m = PyMouse()              # 鼠标的实例m
k = PyKeyboard()           # 键盘的实例k


def get_screen_size():
    """
    获取屏幕尺寸（一般为电脑屏幕的分辨率，如1920*1080）
    """
    return m.screen_size()


def move_mouse(x, y):
    """
    将鼠标移动到位（此步可忽略，直接单击也可）
    """
    m.move(10, 500)


def click_mouse(x, y, tp=1, times=1):
    """
    x y   : 坐标
    tp    : 1 = left, 2 = right, 3 = middle.
    times : 单击次数
    """
    m.click(x, y, tp, times)


def send_key(key):
    """
    模拟键盘键
    """
    k.tap_key(key)


def send_press_key(key):
    """
    模拟键盘按键
    """
    k.press_key(key)


def send_release_key(key):
    """
    模拟键盘松开键
    """
    k.release_key(key)


def press_alt():
    """
    按住alt键
    """
    k.press_key(k.alt_key)


def release_alt():
    """
    松开alt键
    """
    k.release_key(k.alt_key)


def send_string(str):
    """
    模拟键盘输入字符串
    """
    k.type_string(str)


def send_keys(key, num, time):
    """
    模拟点击key键，num次，每次间隔time秒
    """
    k.tap_key(key, n=num, interval=time)


def send_f_key(key):
    """
    点击功能键FX
    """
    k.tap_key(k.function_keys[key])


def send_num_key(key, num=1):
    """
    点击小键盘key,num次
    """
    k.tap_key(k.numpad_keys[key], num)


if __name__ == "__main__":
    x_dim, y_dim = get_screen_size()
    print(x_dim)
    print(y_dim)
