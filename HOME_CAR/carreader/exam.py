import pytesseract
import cv2

# 이미지 불러오기
img = cv2.imread("sample.png", cv2.IMREAD_COLOR)

# 이미지 전처리 (예: 그레이스케일 변환)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

config1 = ('-l kor --psm 7 --oem 0')
# 이미지에서 텍스트 추출
result = pytesseract.image_to_string(gray,config=config1)
print(result)