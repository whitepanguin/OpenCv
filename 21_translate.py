import cv2
import numpy as np

img = cv2.imread('./images/dog.bmp')
aff = np.array([
    [1, 0, 150],
    [0, 1, 100]
], dtype=np.float32)

# 어파인 변환
# 이미지의 위치나 모양을 변경하는 선형 변환
# (0, 0) 어디를 중심으로 할거야 설정, 원본 이미지 크기를 그대로 전달
dst1 = cv2.warpAffine(img, aff, (0,0))

# interpolation(보간법): 픽셀을 어떻게 채울지 결정
# INTER_NEAREST: 최근법 이웃 보간(속도 빠름, 품질 낮음), 가까운 픽셀 값을 그대로 복사. 계단 현상이나 노이즈가 생길 수 있음
dst2 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_NEAREST)
# INTER_CUBIC: 4차 보간법(속도 느림, 품질 좋음), 주변 16개 픽셀을 사용하여 곡선으로 예측, 이미지를 부드럽게 확대/축소
dst3 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

cp = (img.shape[1]/2, img.shape[0]/2)
# 30도 0.7 스케일 해줘서 행렬을 만듬
rot = cv2.getRotationMatrix2D(cp, 30, 0.7)
dst4 = cv2.warpAffine(img, rot, (0,0))


cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()
