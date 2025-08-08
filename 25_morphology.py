import cv2
import numpy as np

# 모폴로지 연산
# 영상 처리에서 형태(Shape) 기반으로 이미지를 다루는 기법
# 특히 이진 영상, 흑백 영상에서 물체의 외곽선 크기, 형태를 변경하거나 분석하는데 사용

# 팽창
# 밝은 영역을 넓히는 연산
# 흰색 물체가 커짐, 구멍이 메워짐
# 얇은 부분이 굵어짐

# 침식 
# 밝은 영역을 줄이는 연산
# 흰색 물체가 작아짐
# 가느다란 연결부가 끊어짐, 노이즈가 제거됨

# 열림
# 침식 후 팽창: 작은 노이즈를 제거한 후 얇은 부분이 굵어짐

# 닫힘
# 팽창 후 침식: 구멍이 메움

img = cv2.imread('./images/circuit.bmp', cv2.IMREAD_GRAYSCALE)
# MORPH_RECT: 사각형, MORPH_ELLIPSE: 타원, MORPH_CROSS: 십자

# gse = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# gse = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) # 훨신더 침식 팽창을 하게 된다
# gse = cv2.getStructuringElement(cv2.MORPH_RECT,(7,3)) # 가로 7 세로 3
gse = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)) # 일반적으로 사각형만 쓰긴 한다
dst1 = cv2.dilate(img, gse) # 팽창
dst2 = cv2.erode(img, gse) # 침식



cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()

