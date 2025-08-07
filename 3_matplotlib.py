import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR)

img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img_color) # bgr로 하면 색이 이상하게 나온다
plt.show()