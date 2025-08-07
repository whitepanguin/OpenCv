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
'''
dst3 = cv2.GaussianBlur(img, (0,0),2)
dst4 = cv2.medianBlur(img, 7)
dst5 = cv2.bilateralFilter(img, 12, 100, 100)
med_val = np.median(img) # 이미지에 전체 평균
lower = int(max(0, 0.7*med_val))
upper = int(min(255, 1.3*med_val))
print(lower)
print(upper)
dst6 = cv2.GaussianBlur(img, (3, 3), 0)
dst6 = cv2.Canny(dst6, lower, upper, 3)
'''
select = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    key = cv2.waitKey(int(1000 / fps))

    if key == ord('b') or key == ord('b'):
        if select != 1:
            select = 1
        else:
            select = 0
    elif key == ord('g') or key == ord('G'):
        if select != 2:
            select = 2
        else:
            select = 0
    elif key == 27:
        break

    if select == 1:
        frame = cv2.blur(frame, (9, 9))
        cv2.putText(frame, 'Blur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 2:
        frame = cv2.GaussianBlur(frame, (0,0),2)
        cv2.putText(frame, 'GaussianBlur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))


    cv2.imshow('frame', frame)
cap.release()