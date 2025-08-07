import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('./images/candies.png', cv2.IMREAD_GRAYSCALE)

# 히스토그램
# 이미지 히스토그램: 밝기(또는 색상) 값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# images: 대상 이미지 리스트
# channel: 분석할 채널 번호(B:0, G:1, R:2)
# mask: 분석할 영역의 마스크(None: 전체)
# histSize: 히스토그램의 빈 개수 (0~255이니까 256개)
# ranges: 값의 범위
hist1 = cv2.calcHist([img1],[0],None,[256],[0,255])


plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(hist1,color='gray')

img2 = cv2.imread('./images/candies.png')


print('shape: ', img2.shape)
print('dtype: ', img2.dtype)
'''
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
'''
hist2 = cv2.calcHist([img2],[0],None,[256],[0,255])
hist3 = cv2.calcHist([img2],[1],None,[256],[0,255])
hist4 = cv2.calcHist([img2],[2],None,[256],[0,255])
colors = ['b','g','r']
channels = cv2.split(img2)
plt.figure(figsize=(10,4))
plt.subplot(1,2,2)
for ch, color in zip(channels, colors):
    hist = cv2.calcHist([ch],[0], None, [256],[0,255])
    plt.plot(hist, color= color, label=color.upper())
# 해당 색이면 그 색의 이미지는 밝게 나옴
b,g,r = cv2.split(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
# plt.plot(hist1, 'y',label="NColor")
# plt.plot(hist2, 'b',label="B")
# plt.plot(hist3, 'g',label="G")
# plt.plot(hist4, 'r',label="R")

plt.show()
cv2.waitKey()

'''
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('./images/candies.png', cv2.IMREAD_GRAYSCALE)
# 히스토그램
# 이미지 히스토그램: 밝기(또는 색상) 값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# images: 대상 이미지 리스트
# channel: 분석할 채널 번호(B:0, G:1, R:2)
# mask: 분석할 영역 마스크(None: 전체)
# histSize: 히스토그램의 빈 개수
# ranges: 값의 범위
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(hist1, color='gray')
img2 = cv2.imread('./images/candies.png')
print('shape: ', img2.shape)
print('dtype: ', img2.dtype)
''''''
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
''''''
colors = ['b', 'g', 'r']
channels = cv2.split(img2)
plt.subplot(1, 2, 2)
for ch, color in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 255])
    plt.plot(hist, color=color, label=color.upper())
b, g, r = cv2.split(img2)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
plt.plot(hist1)
plt.show()
cv2.waitKey()
'''