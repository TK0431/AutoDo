import _thread

map_type = 0
road_type = 0
pos = (0,0)

def pic_start(img):
    pos = get_pos(img)
    tp = judge_back(img)
    if tp > 0:
        pass
    elif tp < 0:
        pass
    else:
        pass
    #_thread.start_new_thread(press_a)
    #_thread.start_new_thread(press_w)
    #flg = False

def get_pos(img):
    return (0,0)

def judge_back(img) -> int:
    return 0

def room_work(img):
    mask_list = judge_mast(img)
    if(len(mask_list) > 0):
        mask_work(img,mask_list)
    else:
        find_door(img)

def judge_mast(img) -> []:
    ls = []
    ls.append((122,24))
    return ls

def mask_work(img,ls):
    pass

def find_door(img):
    pass