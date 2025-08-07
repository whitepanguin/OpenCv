import cv2

cap1 = cv2.VideoCapture('./movies/woman.mp4')
cap2 = cv2.VideoCapture('./movies/sea.mp4')

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps = cap1.get(cv2.CAP_PROP_FPS)

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    ret2, frame2 = cap2.read()
    if not ret1:
        break

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
    cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame1', frame1)
    if cv2.waitKey(10) == ord(' '):
        cv2.waitKey()
    elif cv2.waitKey(10) == 27:
        break
cap1.release()
cap2.release()

