import cv2

# ROI(Region of Interest): 관심 영역
img = cv2.imread('./images/sun.jpg')

x = 182
y = 22
w = 119
h = 108

roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()
img[y:y+h,x+w:x+w+w] = roi
# cv2.rectangle(img, (x, y, 240, 108),(0, 255, 0), 2)
cv2.rectangle(img, (x, y), (x+w+w, y+h),(0, 255, 0), 3)

oldx = oldy = 0

# flags 는 상태 채크하고 있는 애
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        roi = img[oldy:y, oldx:x]
        roi_copy = roi.copy()
        cv2.imshow('cut',roi_copy)
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (oldx, oldy), (x,y), (0, 255, 0), 1)
            cv2.imshow('img', img_copy)


cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()
