import cv2
import numpy as np

img = cv2.imread('./images/namecard.jpg')

cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)

pic_h, pic_w = img.shape[:2]
r = 20
tl = (r, r)
tr = (pic_w-r, r)
bl = (r, pic_h-r)
br = (pic_w-r, pic_h-r)
w, h = 600, 400

oldx = oldy = 0
select = 0
def is_in_circle(cx,cy,r,px,py):
    dx = px - cx
    dy = py - cy
    return dx * dx + dy * dy <= r*r

def on_mouse(event, x, y, flags, param):
    global oldx, oldy, w, h, tl, tr, bl, br, r, select
    img_copy = img.copy()
    cv2.circle(img_copy, tl, r, (0, 0, 255), -1)
    cv2.circle(img_copy, tr, r, (0, 0, 255), -1)
    cv2.circle(img_copy, bl, r, (0, 0, 255), -1)
    cv2.circle(img_copy, br, r, (0, 0, 255), -1)
    cv2.line(img_copy, tl, tr, (0, 255, 0), 2)
    cv2.line(img_copy, tr, br, (0, 255, 0), 2)
    cv2.line(img_copy, br, bl, (0, 255, 0), 2)
    cv2.line(img_copy, bl, tl, (0, 255, 0), 2)
    cv2.imshow('img',img_copy)
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어요: %d, %d'% (x,y))
        oldx, oldy = x, y
        if is_in_circle(*tl,r,x,y):
            print(1)
            select = 1
        if is_in_circle(*tr,r,x,y):
            print(2)
            select = 2
        if is_in_circle(*bl,r,x,y):
            print(3)
            select = 3
        if is_in_circle(*br,r,x,y):
            print(4)
            select = 4
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떄졌어요: %d, %d'% (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스가 이동하고 있어요: %d, %d'% (x, y))
        if flags & cv2.EVENT_FLAG_LBUTTON:
            print('마우스를 드래그 하고 있어요')
            if select==1:
                tl = (x, y)
            if select==2:
                tr = (x, y)
            if select==3:
                bl = (x, y)
            if select==4:
                br = (x, y)
            cv2.imshow('img',img_copy)

srcQuad = np.array(
    [[370, 173],[1224, 157],[1417, 830],[209, 849]], np.float32
)
dstQuad = np.array(
    [[0, 0],[w, 0],[w, h],[0, h]], np.float32
)
# 투시 변환(Perspective Transform)
# 영상에서 원근감을 조절하거나, 사각형을 반듯하게 펴주는 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(img, pers, (w, h))

cv2.imshow('img',img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()