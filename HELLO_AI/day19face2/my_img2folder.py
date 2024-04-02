# 0 김민경
# 1 김승연
# 2 김차은
# 3 김창용
# 4 김초희
# 5 김현우
# 6 남희수
# 7 박주호
# 8 박지원
# 9 배유림
# 10 백영웅
# 11 변상원
# 12 송은비
# 13 우민규
# 14 유길상
# 15 이미소
# 16 이상철
# 17 이성휘
# 18 정민지
# 19 하예종
import cv2

print(cv2.__version__)

image = cv2.imread('k.png')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for idx,(x, y, w, h) in enumerate(faces):
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face_img = image[y:y+h, x:x+w]
    cv2.imwrite("{}.png".format(idx), face_img)


cv2.imshow('k', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
import os
files=os.listdir('img')

for idx,fn in enumerate(files):
    str_cnt=str(idx+100)[1:]
    # os.mkdir("pre01/{}".format(str(idx+100)[1:]))
    # print(idx,fn.replace('.mp4',''))
    print("{{'lbl':'{}','f':'{}','n':'{}'}},".format(idx,str_cnt,fn.replace('.mp4','')))