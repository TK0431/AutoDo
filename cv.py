import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_img(path):
    """
    读取图片
    """
    return cv2.imread(path)


def debug_show_img(img, title="debug"):
    """
    窗体显示图片
    """
    cv2.imshow(title, img)


def save_img(img, path):
    """
    图片保存
    """
    cv2.imwrite(path, img)

def get_cvt_image(img, cvt):
    """
    单色通道
    """
    return cv2.cvtColor(img,cvt)


def get_blur_image(img):
    """
    图像模糊
    """
    return cv2.GaussianBlur(img,(7,7),0)


def get_canny_image(img):
    """
    边缘检测
    """
    return  cv2.Canny(img, 100, 100)

def get_dilate_image(img):
    """
    膨胀
    """
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(img,kernel,iterations=1)

def get_erode_image(img):
    """
    侵蚀
    """
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(img,kernel,iterations=1)

def get_image_shape(img):
    return img.shape

def resize_image(img):
    return cv2.resize(img,(300,200))

def crop_image(img):
    return img[100:700,100:700]

def range_image():
    img = np.zeros((512,512,3),np.uint8)
    #img[200:300,100:400] = 255,0,0
    cv2.line(img,(0,0),(300,300),(0,255,0),1)
    cv2.rectangle(img,(0,0),(250,350),(0,0,255),1)
    cv2.circle(img,(400,50),30,(255,255,0),2)
    cv2.putText(img," OPEN CV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),1)
    return img

def get_1(img):
    #w,h,_ = img.shape
    pts1 = np.float32([[533,39],[985,331],[541,1027],[81,751]])
    pts2 = np.float32([[0,0],[250,0],[250,350],[0,350]]) 
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    return cv2.warpPerspective(img,matrix,(250,350))

def get_2(img):
    hor = np.hstack((img,img))
    return np.vstack((hor,hor))

def get_3(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    return imgHSV

def get_4(img):
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
    cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
    cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
    cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

    while True:
        img1 = read_img(r"D:\2.jpg") # 读取图片
        imgHSV = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
        v_min = cv2.getTrackbarPos("Val Min","TrackBars")
        v_max = cv2.getTrackbarPos("Val Max","TrackBars")
        print(h_min,h_max,s_min,s_max,v_min,v_max)
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        mask = cv2.inRange(imgHSV,lower,upper)
        imgResult = cv2.bitwise_and(img1,img1,mask = mask)

        debug_show_img(imgHSV)
        debug_show_img(mask,"1")
        debug_show_img(imgResult,"2")
        cv2.waitKey(1)

def empty(a):
    pass


def get_5(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    debug_show_img(imgGray,"1")
    debug_show_img(imgBlur,"2")
    debug_show_img(imgCanny,"3")

    img0 = img.copy()
    c,h = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in c:
        area = cv2.contourArea(cnt)
        #print(area)
        #cv2.drawContours(img0,cnt,-1,(255,0,0),3)
        if area > 500:
            cv2.drawContours(img0,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.015*peri,True)
            objCor = len(approx)
            print(objCor)
            x,y,w,h = cv2.boundingRect(approx)

            if objCor == 4:
                objectType = "Tri"
            else:
                objectType = "None"

            cv2.rectangle(img0,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img0,objectType,
                (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),2)


    debug_show_img(img0,"4")

if __name__ == "__main__":
    img = read_img(r"D:\2.jpg") # 读取图片
    print(get_image_shape(img))

    # gray = get_cvt_image(img, cv2.COLOR_BGR2GRAY) # 彩色图片灰度化
    # blur = get_canny_image(img)
    # canny = get_canny_image(img)
    # dilate = get_dilate_image(img)
    # erode = get_erode_image(img)
    # resize = resize_image(img)
    # crop = crop_image(img)
    # rang = range_image()
    # g1 = get_1(img)
    # g2 = get_2(img)
    # g3 = get_3(img)
    g5 = get_5(img)

    #debug_show_img(edges,"1")
    # plt.subplot(121)
    # plt.imshow(edges)

    # 执行Hough直线检测
    # lines = cv2.HoughLines(edges, 1, np.pi/180, 160)
    # lines1 = lines[:, 0, :]
    # for rho, theta in lines1:
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a*rho
    #     y0 = b*rho
    #     x1 = int(x0 + 1000*(-b))
    #     y1 = int(y0 + 1000*(a))
    #     x2 = int(x0 - 1000*(-b))
    #     y2 = int(y0 - 1000*(a))
    #     cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

    # debug_show_img(img,"2")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # plt.subplot(122)
    # plt.imshow(img)
