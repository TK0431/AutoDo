from help_cv import *
from help_user32 import *



hwnd = get_hwnd(None,"Notepad")

img = read_hwnd0_img(hwnd)
#img = read_hwnd_size_img(hwnd)
#img = read_hwnd_img(hwnd)
#img0 = read_qt5_img(img)
img = read_qt5_img(img)

save_img(img,r"D:\12.jpg")

debug_show_img(img)



cv2.waitKey(1)

