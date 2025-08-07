import cv2

# 해상도가 동일해야한다
cap1 = cv2.VideoCapture('./movies/11tiny.mp4')
cap2 = cv2.VideoCapture('./movies/13tiny.mp4')

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

print(w, h)
print(frame_cnt1, frame_cnt2)
print(fps1, fps2)

# bmp 데이터 그대로 저장, 그래서 영상들은 다 압축 기술들이다.
#동영상을 만드는 역활 DIVX => avi
fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('mix.avi',fourcc, fps1, (w, h))

for i in range(frame_cnt1):
    ret, frame = cap1.read()
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()