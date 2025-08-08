import cv2

# 라벨링
# 이미지 속에서 연결된 픽셀 덩어리를 찾아서 각각에 번호를 붙이는 작업
# 이진 영상에서 사용되며, 물체별로 분리, 개수 세기, 위치 분석 등에 활용

# 라벨링 과정
# 1. 이진화: 흑백으로 변환
# 2. 픽셀 그룹 찾기: 상, 하, 좌, 우 방향으로 연결된 그룹, 대각선까지 포함한 그룹
# 3. 각 그룹에 라벨 번호를 부여
# 4. 각 객체의 위치, 크기, 면적, 중심점 등을 구함

img = cv2.imread('./images/keyboard.bmp', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # 아님 상자 오류남

# connectedComponentsWithStats: 한 번에 라벨링과 통계값 계산
# cnt: 찾은 객체 개수(배경 포함)
# labels: 각 픽셀의 라벨 번호가 저장된 2D 배열
# stats: 각 객체의 [x, y, width, height, area] 정보 (바운딩 박스로 나온다) area는 픽셀 개수
# centroids: 각 객체의 중심 좌표(부동소수점 값)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)
print(cnt) # 38
print('-'*50)
print(labels)
print('-'*50)
print(stats)
print('-'*50)
print(centroids)
print('-'*50)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]
    if area < 30:
        continue
    cv2.rectangle(dst, (x, y, w, h),(0, 255, 255))

cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()