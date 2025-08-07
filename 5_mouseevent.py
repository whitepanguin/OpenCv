import cv2
import numpy as np

oldx = oldy = 0


# flags 는 상태 채크하고 있는 애
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어요: %d, %d'% (x,y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떄졌어요: %d, %d'% (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스가 이동하고 있어요: %d, %d'% (x, y))
        if flags & cv2.EVENT_FLAG_LBUTTON:
            print('마우스를 드래그 하고 있어요')
            cv2.line(img, (oldx, oldy), (x,y), (255, 255, 255), 2)
            cv2.imshow('img', img)
            oldx, oldy = x, y

img = np.ones((500,500,3), dtype=np.uint8) * 2
# img2 = np.ones((500,500,3), dtype=np.uint8) *128

cv2.namedWindow('img') #이건 확실한 방법

cv2.rectangle(img, (50, 200, 150, 100),(0, 255, 0), 3)
cv2.rectangle(img, (300, 200, 150, 100),(0, 255, 0), -1) # 가로에서부터 300 위에서 200, 가로 세로 150 100

cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)

cv2.putText(img, 'Hello', (50, 300), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))

cv2.imshow('img',img)
# cv2.imshow('img',img2)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()
