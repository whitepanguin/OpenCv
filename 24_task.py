import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

cap = cv2.VideoCapture('./movies/camera.avi')

if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()
print('동영상을 불러올 수 있음')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'동영상 사이즈: {width} x {height}')
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

def onMouse(event, x, y, flags, param):
    global 

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i]-(x,y))< 25:
                dragSrc[i] = True
                ptOld = (x, y)
                break
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                srcQuad[i] = (x, y)
                cpy = drawROI(img, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x,y)
                break
    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i]= False

select = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    key = cv2.waitKey(int(1000 / fps))

    if key == ord('h') or key == ord('H'):
        if select != 20:
            select = 20
        else:
            select = 0
    elif key == ord('b') or key == ord('b'):
        if select != 1:
            select = 1
        else:
            select = 0
    elif key == ord('g') or key == ord('G'):
        if select != 2:
            select = 2
        else:
            select = 0
    elif key == ord('m') or key == ord('M'):
        if select != 3:
            select = 3
        else:
            select = 0
    elif key == ord('f') or key == ord('F'):
        if select != 4:
            select = 4
        else:
            select = 0
    elif key == ord('c') or key == ord('C'):
        if select != 5:
            select = 5
        else:
            select = 0
    elif key == ord('1'):
        if select != 10:
            select = 10
        else:
            select = 0
    elif key == 27:
        break

    if select == 20:
        cv2.putText(frame, 'Help ❓', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
        cv2.putText(frame, 'b: Blur g:GaussianBlur m:MedianBlur', (10, 60), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
        cv2.putText(frame, 'f: BilateralFilter c:CannyEdge', (10, 90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 1:
        frame = cv2.blur(frame, (9, 9))
        cv2.putText(frame, 'Blur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 2:
        frame = cv2.GaussianBlur(frame, (0,0),4)
        cv2.putText(frame, 'GaussianBlur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 3:
        frame = cv2.medianBlur(frame, 9)
        cv2.putText(frame, 'MedianBlur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 4:
        frame = cv2.bilateralFilter(frame, 12, 100, 100)
        cv2.putText(frame, 'BilateralFilter', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 5:
        med_val = np.median(frame) 
        lower = int(max(0, 0.15*med_val))
        upper = int(min(255, 1.85*med_val))
        frame = cv2.GaussianBlur(frame, (3, 3), 0)
        frame = cv2.Canny(frame, lower, upper, 1)
        cv2.putText(frame, 'CannyEdge', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 10:
        frame_copy = frame.copy()
        cv2.setMouseCallback('frame',onMouse)
        frame = cv2.bilateralFilter(frame, 12, 100, 100)
        cv2.putText(frame, 'BilateralFilter', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))


    cv2.imshow('frame', frame)
cap.release()