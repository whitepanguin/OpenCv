import cv2
import numpy as np

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img_gif = cv2.imread('./images/week.gif', cv2.IMREAD_GRAYSCALE)

print('img_gray type: ', type(img_gray)) # ndarray
print('img_gray shape: ', img_gray.shape) # 세로 가로
print('img_gray dtype: ', img_gray.dtype) # uint8 부호 없는 0~255

img_color = cv2.imread('./images/dog.bmp')

print('img_color type: ', type(img_color)) # ndarray
print('img_color shape: ', img_color.shape) # 세로 가로 색상
print('img_color dtype: ', img_color.dtype) # uint8 부호 없는 0~255

h, w = img_color.shape[:2]
print(f'이미지 사이즈: {w} * {h}')

if len(img_color.shape)== 3:
    print('컬러 영상')
elif len(img_color.shape) ==2:
    print('그레이스케일 영상')

img1 = np.zeros((240,320,3), dtype=np.uint8)
img2 = np.empty((240, 320), dtype=np.uint8)
img3 = np.ones((240, 320), dtype=np.uint8) * 120
img4 = np.full((240, 320, 3), (225, 102, 225), dtype=np.uint8)

# for x in range(h):
#     for y in range(w):
#         img_color[x, y] = (255, 102, 255)
# 위랑 같은 코드다
img1[:,:] = (225, 102, 225)

cv2.imshow('img_color', img_color)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.imshow('img_gif', img_gif)

while True:
    keyvalue = cv2.waitKey()
    # 아스킷코드값을 변환해준다
    if keyvalue == ord('i') or keyvalue == ord('I'):
        #값을 반전하라
        img_color = ~img_color
        cv2.imshow('img_color',img_color)
    elif keyvalue == 27:
        #esc키임
        break