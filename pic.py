from PIL import ImageGrab


def get_pic_byte(x, y, w, h):
    return ImageGrab.grab(bbox=(x, y, w, h))


def save_pic(x, y, w, h, path):
    pic = get_pic_byte(x, y, w, h)
    pic.save(path)

if __name__ == "__main__":
    pic=get_pic_byte(0, 0, 200, 100)
    pic.save(r"D:\4.jpg")
