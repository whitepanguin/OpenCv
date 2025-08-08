import cv2 
import math

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w , y+h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 2)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))

img = cv2.imread('./images/polygon.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# THRESH_BINARY_INV: 임계값 이상이면 검정(0), 임계값 미만이면 흰색(255)
_,img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for pts in contours:
    if cv2.contourArea(pts) < 50:
        continue
    # approxPolyDP: 꼭짓점의 개수를 줄여서 간단한 규칙 기반 분류를 해준다. 픽셀이 어느정도 나갔는지 계산해서 직선화 해주는 것
    # arcLength: 둘레
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)* 0.02, True)
    print(approx)
    vtc = len(approx)
    print(vtc) # 꼭지점 개수

    if vtc ==3:
        setLabel(img, pts, 'TRI')
    elif vtc ==4:
        setLabel(img, pts, 'RECT')
    else:
        length = cv2.arcLength(pts,True)
        area = cv2.contourArea(pts)
        # 4*math.pi* area / (length * length): 원형도를 구함
        # 값의 범위: 0~1, 1에 가까울수록 원에 가까움
        ratio = 4. * math.pi * area / (length * length)
        if ratio > 0.8:
            setLabel(img, pts, 'CIR')
        else:
            setLabel(img, pts, 'NONAME')

cv2.imshow('img', img)
cv2.waitKey()