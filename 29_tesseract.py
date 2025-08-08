# OCR(Optical Character Regognition) 광학문자인식
# 영상이나 문서에서 텍스트를 자동으로 인식하고 컴퓨터가 이행할 수 있는 텍스트 데이터로 변환하는 과정
# Tesseract, EasyOCR, PaddleOCR, CLOVA OCR(네이버 API), Cloud Vision(구글 API) ..

# 테서렉트
# https://github.com/UB-Mannheim/tesseract/wiki

import cv2
import pytesseract

img = cv2.imread('./images/hello.png')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# lang='kor', lang='eng, lang='kor+eng'
text = pytesseract.image_to_string(dst, lang='kor+eng')
print(text)

cv2.imshow('img',img)
cv2.waitKey()