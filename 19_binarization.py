import cv2
import matplotlib.pyplot as plt

# 이진화
# 이미지의 픽셀 값을 0과 1(0과 255) 두 가지 값만 가지도록 만드는 영상 처리 기법
# OCR, 윤곽 검출, 객체 분할, 문서 스켄 등 작업에 유리

img = cv2.imread('./images/cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img],[0],None, [256],[0,255])

# 임계값인 100을 넘으면 255로 설정
# 픽셀값이 임계값을 넘으면 최대값으로 설정하고, 넘지 못하면 0으로 설정
a, dst1 = cv2.threshold(img, 100,255,cv2.THRESH_BINARY)
print(a)
b, dst2 = cv2.threshold(img, 210,255,cv2.THRESH_BINARY)
print(b)
# 자동으로 임계값을 찾아주긴함 하지만, 전체 계산을 한거라 밝고 어둡고가 있으면 잘 못 찾는 상황도 발생한다
c, dst3 = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(c) 


cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
plt.plot(hist)
plt.show()
cv2.waitKey()