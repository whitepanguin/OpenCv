import cv2

oldx = oldy = w = h = 0
color = (255, 0 , 0)
isDrag = False
img_copy = None

def on_mouse(event, x,y,flags, param):
    global oldx, oldy, w, h, isDrag, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        isDrag = True
        oldx = x
        oldy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDrag:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (oldx, oldy), (x, y), color, 3)
            cv2.imshow('img',img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDrag:
            isDrag = False
            if x > oldx and y > oldy:
                w = x - oldx
                h = y - oldy
                if w > 0 and h > 0:
                    cv2.rectangle(img_copy, (oldx, oldy), (x, y), color, 3)
                    cv2.imshow('img', img_copy)
                    roi = img[oldy:oldy+h, oldx: oldx+w]
                    cv2.imshow('roi',roi)
        else:
            cv2.imshow('img', img)
            print('영역이 설정되지 않음')



img = cv2.imread('./images/sun.jpg')

cv2.namedWindow('img')
cv2.setMouseCallback('img',on_mouse)
cv2.imshow('img',img)
cv2.waitKey()