import cv2
import random
import numpy as np

# 외각선
# 영상에서 같은 색 또는 강도를 가진 경계선을 추적해 얻는 죄표 집합
# 영상 분석에서 물체의 모양, 크기, 위치를 찾을 때 유용
img = cv2.imread('./images/contours.bmp', cv2.IMREAD_GRAYSCALE)

# img: 이진 이미지 사용
# mode: 컨투어 추출 방식
# RETR_CCOMP: 2계층 구조로 모든 컨투어 추출 (박스안 박스 까지만 추출)
# RETR_LIST: 모든 컨투어 추출
# RETR_EXTERNAL: 최외곽 컨투어만 추출
# RETR_TREE: 모든 컨투어를 트리 구조로 추출(복잡한 계층 정보 포함)

# method: 컨투어 근사화 방식
# CHAIN_APPROX_NONE: 모든 경계 좌표 저장(정밀하지만 데이터 큼)
# CHAIN_APPROX_SIMPLE: 직선 구간은 시작/끝만 저장(효율적)

# contours: 외각선의 좌표 목록(리스트)

# hierarchy: 계층 관계를 나타내는 배열
# hierarchy[0][i]: [next, prev, child, parent]
# next: 같은 계층 레벨에서 다음 컨투어의 인덱스(없으면 -1)
# prev: 같은 계층 레벨에서 이전 컨투어의 인덱스(없으면 -1)
# child: 하위(내부) 컨투어의 인덱스(없으면 -1)
# parent: 상위(외부) 컨투어의 인덱스(없으면 -1)
contours, hierarchy = cv2.findContours(img,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# print(contours)
# print(hierarchy)

dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# 전체 외각선을 한 번에 그림
cv2.drawContours(dst, contours, -1, color, 3)
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()