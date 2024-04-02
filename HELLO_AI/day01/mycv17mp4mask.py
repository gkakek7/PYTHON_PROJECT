import cv2
import numpy as np

video = "sarang.mp4"  # 동영상 파일 경로

img = cv2.imread('mask/118.png', cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(video)  # 동영상 캡처 객체 생성

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                # 얼굴 크기에 맞게 PNG 이미지 크기를 조절
                resized_img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)

                # 알파 채널을 이용하여 투명한 부분을 고려하여 이미지를 합성
                alpha_channel = resized_img[:, :, 3] / 255.0
                for c in range(0, 3):
                    frame[y:y + h, x:x + w, c] = frame[y:y + h, x:x + w, c] * (1 - alpha_channel) + \
                                                  resized_img[:, :, c] * alpha_channel

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()