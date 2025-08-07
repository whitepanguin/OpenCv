import cv2
import sys
import time

cap = cv2.VideoCapture('./movies/11tiny.mp4')

if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()

print('동영상을 불러올 수 있음')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(width)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height)
print(f'동영상 사이즈: {width} x {height}')

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count) # 영상에 쓰인 이미지 수

# fps frame per sec
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps) # 1초에 24이미지가 지나간다

while True:
    # cap.read() 프레임 한장을 가져오는 거다
    # ret 정상적으로 가져온건지,
    # frame 한장에 대한 이미지 데이터 ndarray
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    # 10 = 0.01초 안에 27을 누르지 않으면 계속 넘어간다.
    # int(1000 / fps) 하면 원래 영상 속도로 나온다
    if cv2.waitKey(int(1000 / fps)) == 27:
        break
cap.release()

