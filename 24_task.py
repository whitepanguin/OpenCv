import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import random

# 도형 클래스
class Shape:
    def __init__(self, x, y, w=60, h=60, color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), shape_type='rect'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.dragging = False
        self.shape_type = shape_type

    def draw(self, frame):
        if self.shape_type == 'rect':
            cv2.rectangle(frame, (self.x, self.y), (self.x + self.w, self.y + self.h), self.color, -1)

        elif self.shape_type == 'circle':
            center = (self.x + self.w // 2, self.y + self.h // 2)
            radius = min(self.w, self.h) // 2
            cv2.circle(frame, center, radius, self.color, -1)

        elif self.shape_type == 'heart':
            self.draw_heart(frame)

    def draw_heart(self, frame):
        pts = np.array([
            [self.x + self.w//2, self.y + self.h],# 아래점
            [self.x, self.y + self.h//2],# 좌측 중간
            [self.x + self.w//4, self.y],# 좌측 위
            [self.x + self.w//2, self.y + self.h//4],# 중앙 위
            [self.x + 3*self.w//4, self.y],# 우측 위
            [self.x + self.w, self.y + self.h//2]# 우측 중간
        ], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(frame, [pts], self.color)

    def is_inside(self, px, py):
        if self.shape_type == 'rect':
            return self.x <= px <= self.x + self.w and self.y <= py <= self.y + self.h
        elif self.shape_type == 'circle':
            cx = self.x + self.w // 2
            cy = self.y + self.h // 2
            radius = min(self.w, self.h) // 2
            return (px - cx) ** 2 + (py - cy) ** 2 <= radius ** 2
        elif self.shape_type == 'heart':
            return self.x <= px <= self.x + self.w and self.y <= py <= self.y + self.h

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# 도형 리스트 및 선택 상태 변수
shapes = []

selected_shape = None
prev_mouse_pos = None

# 마우스 이벤트 함수
def onMouse(event, x, y, flags, param):
    global selected_shape, prev_mouse_pos

    if event == cv2.EVENT_LBUTTONDOWN:
        for shape in reversed(shapes):
            if shape.is_inside(x, y):
                selected_shape = shape
                shape.dragging = True
                prev_mouse_pos = (x, y)
                break

    elif event == cv2.EVENT_MOUSEMOVE and selected_shape and selected_shape.dragging:
        dx = x - prev_mouse_pos[0]
        dy = y - prev_mouse_pos[1]
        selected_shape.move(dx, dy)
        prev_mouse_pos = (x, y)

    elif event == cv2.EVENT_LBUTTONUP and selected_shape:
        selected_shape.dragging = False
        selected_shape = None

cap = cv2.VideoCapture('./movies/camera.avi')

if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()
print('동영상을 불러올 수 있음')
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', onMouse)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'동영상 사이즈: {width} x {height}')
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

select = 0

fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('filter.avi',fourcc, fps, (int(width), int(height)))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    key = cv2.waitKey(int(1000 / fps))

    if key == ord('h') or key == ord('H'):
        if select != 20:
            select = 20
        else:
            select = 0
    elif key == ord('b') or key == ord('b'):
        if select != 1:
            select = 1
        else:
            select = 0
    elif key == ord('g') or key == ord('G'):
        if select != 2:
            select = 2
        else:
            select = 0
    elif key == ord('m') or key == ord('M'):
        if select != 3:
            select = 3
        else:
            select = 0
    elif key == ord('f') or key == ord('F'):
        if select != 4:
            select = 4
        else:
            select = 0
    elif key == ord('c') or key == ord('C'):
        if select != 5:
            select = 5
        else:
            select = 0
    elif key == ord('1'):
        shapes.append(Shape(40, 40, shape_type='rect', color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))))
    elif key == ord('2'):
        shapes.append(Shape(100, 40, shape_type='circle', color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))))
    elif key == ord('3'):
        shapes.append(Shape(160, 40, shape_type='heart', color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))))
    elif key == 27:
        break

    if select == 20:
        cv2.putText(frame, 'Help ❓', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
        cv2.putText(frame, 'b: Blur g:GaussianBlur m:MedianBlur', (10, 60), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
        cv2.putText(frame, 'f: BilateralFilter c:CannyEdge', (10, 90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
        cv2.putText(frame, '1: Rect 2:Cir 3:Heart', (10, int(height)-20), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 1:
        frame = cv2.blur(frame, (9, 9))
        cv2.putText(frame, 'Blur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 2:
        frame = cv2.GaussianBlur(frame, (0,0),4)
        cv2.putText(frame, 'GaussianBlur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 3:
        frame = cv2.medianBlur(frame, 9)
        cv2.putText(frame, 'MedianBlur', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 4:
        frame = cv2.bilateralFilter(frame, 12, 100, 100)
        cv2.putText(frame, 'BilateralFilter', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))
    elif select == 5:
        med_val = np.median(frame) 
        lower = int(max(0, 0.15*med_val))
        upper = int(min(255, 1.85*med_val))
        frame = cv2.GaussianBlur(frame, (3, 3), 0)
        frame = cv2.Canny(frame, lower, upper, 1)
        cv2.putText(frame, 'CannyEdge', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255))

    for shape in shapes:
        shape.draw(frame)

    cv2.imshow('frame', frame)
    write_frame = frame
    if len(frame.shape) == 2:
        write_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    out.write(write_frame)
cap.release()