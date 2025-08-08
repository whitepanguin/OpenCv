import cv2
import numpy as np
import sys
import pytesseract


img = cv2.imread('./images/businesscard2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
h, w = 300, 600
contours, _ = cv2.findContours(img_bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)


for pts in contours:
    if cv2.contourArea(pts) < 5000:
        continue

    cv2.drawContours(img, [pts], -1 , (255, 255, 0), 2)
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)* 0.02, True)
    if len(approx) == 4:
        approx = approx.reshape(4, 2).astype(np.float32)
        def sort_corners(pts):
            pts = sorted(pts, key=lambda x: x[1])  
            top = sorted(pts[:2], key=lambda x: x[0])   
            bottom = sorted(pts[2:], key=lambda x: x[0], reverse=True)  
            return np.array([top[0], top[1], bottom[0], bottom[1]], dtype=np.float32)
        
        srcQuad = sort_corners(approx)
        width_top = np.linalg.norm(srcQuad[0] - srcQuad[1])
        width_bottom = np.linalg.norm(srcQuad[2] - srcQuad[3])
        height_left = np.linalg.norm(srcQuad[0] - srcQuad[3])
        height_right = np.linalg.norm(srcQuad[1] - srcQuad[2])
        w = int(max(width_top, width_bottom))
        h = int(max(height_left, height_right))

        rotate = h > w

        if rotate:
            dstQuad = np.array([[0, 0], [0, w], [h, w], [h, 0]], dtype=np.float32)  
            out_size = (h, w)
        else:
            dstQuad = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)  
            out_size = (w, h)
        pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
        dst = cv2.warpPerspective(img, pers, out_size)
        text = pytesseract.image_to_string(dst, lang='kor+eng')
        print(text)

cv2.imshow('img', img)
cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()