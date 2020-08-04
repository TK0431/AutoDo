import win32gui
import pic


def get_hwnd(name, clss=None):
    return win32gui.FindWindow(clss, name)


def get_win_rect(hwnd):
    """
    left, top, right, bottom
    """
    return win32gui.GetWindowRect(hwnd)


def get_win_size(hwnd):
    """
    width,height
    """
    left, top, right, bottom = get_win_rect(hwnd)
    return right-left, bottom-top


def get_top_hwnd():
    return win32gui.GetForegroundWindow()


def get_hwnd_pic(hwnd):
    left, top, right, bottom = get_win_rect(hwnd)
    if hwnd != get_top_hwnd():
        win32gui.SetForegroundWindow(hwnd)
    # left = 248
    # top = 143
    # right = 1401
    # bottom = 741
    pic.save_pic(left, top, right-left, bottom-top, r"D:\4.jpg")
    print(left)
    print(top)
    print(right)
    print(bottom)
    print(right-left)
    print(bottom-top)


if __name__ == "__main__":
    hwnd = get_hwnd(None,"ConsoleWindowClass")
    print(hwnd)
    print(get_win_rect(hwnd))
    print(get_win_size(hwnd))
    pic.get_pic(hwnd)
    #get_hwnd_pic(hwnd)
    #print(win32gui.FindWindow("无标题 - 记事本", "Notepad"))
