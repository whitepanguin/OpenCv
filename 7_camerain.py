import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없음')
    sys.exit()

print('카메라 연결 성공')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(width)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height)

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    # cap.read() 프레임 한장을 가져오는 거다
    # ret 정상적으로 가져온건지,
    # frame 한장에 대한 이미지 데이터 ndarray
    ret, frame = cap.read()
    if not ret:
        break # 이미지가 없으면 멈춤
    cv2.imshow('frame', frame)
    # 10 = 0.01초 안에 27을 누르지 않으면 계속 넘어간다.
    if cv2.waitKey(10) == 27:
        break
cap.release()