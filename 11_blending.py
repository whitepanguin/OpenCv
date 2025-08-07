import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/turkey.jpg')
img2 = cv2.imread('./images/man.jpg')

# 0 ~ 255값을 벗어나면 256으로 나눈 나머지가 됨
dst1 = img1 + img2

# 0 ~ 255값을 벗어나도 0 또는 255값으로 보정해준다
dst2 = cv2.add(img1, img2)

# cv2.imshow('dst1',dst1)
# cv2.imshow('dst2',dst2)
# cv2.waitKey()

img = {'img1':img1,'img2':img2,'dst1':dst1,'dst2':dst2}
for i,(k, v) in enumerate(img.items()):
    plt.subplot(2,2,i+1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
plt.show()
