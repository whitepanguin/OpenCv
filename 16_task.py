import cv2

cap1 = cv2.VideoCapture('./movies/woman.mp4')
cap2 = cv2.VideoCapture('./movies/sea.mp4')

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

print(w, h)
print(frame_cnt1, frame_cnt2)
print(fps1, fps2)

fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('greenscreen.avi',fourcc, fps1, (w, h))
'''
for i in range(frame_cnt2):
    ret, frame = cap2.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.inRange(hsv, (40, 150, 0), (85, 255, 255))
    temp = cv2.copyTo(frame, dst)
    cv2.imshow('output',temp)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break
'''
while True:
    ret1, frame = cap1.read()
    ret2, backg = cap2.read()

    if not ret1 or not ret2:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (40, 150, 0), (85, 255, 255))
    fg_part = cv2.copyTo(frame, ~mask)
    bg_part = cv2.copyTo(backg, mask)

    final = cv2.add(fg_part, bg_part)

    cv2.imshow('Green Screen', final)
    out.write(final)
    if cv2.waitKey(10) == 27:
        break
cap1.release()
cap2.release()
out.release()
