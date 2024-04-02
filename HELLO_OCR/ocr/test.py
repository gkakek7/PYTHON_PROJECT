from PIL import Image
import pytesseract 
import cv2
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
path="../ocr/img/img2.jpg"

def preprocess_image(path):
    # 이미지 불러오기
    img = cv2.imread(path)
    # 이미지 크기 조정
    resized_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # 흑백으로 변환
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    # 이미지 이진화
    threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # 노이즈 제거
    denoised_img = cv2.fastNlMeansDenoising(threshold_img, None, 10, 7, 21)
    return denoised_img


# 전처리된 이미지 저장
preprocessed_img = preprocess_image(path)
# cv2.imwrite('test_img', preprocessed_img)

img = Image.open(path)
text = pytesseract.image_to_string(img,lang='kor+eng')

print (text)

# 이미지 파일 이름에서 확장자를 제외한 부분 추출하여 파일명 생성
file_name = path.split('/')[-1].split('.')[0]

#
# 텍스트 파일에 결과 저장
with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print(f'결과가 {file_name}.txt 파일로 저장되었습니다.')

