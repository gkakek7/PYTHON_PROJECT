import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time
import cv2
model = tf.keras.models.load_model('cifarteam.h5')
img = cv2.imread("0.jpg")
img=cv2.resize(img,(622,504))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
arr=[]
for (x, y, w, h) in faces:
    img = img[y: y + h, x: x + w]
    cropped_img=cv2.resize(img,(32,32))
    s=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cropped_img=cropped_img.reshape(1,32,32,3)
    pred = model.predict(cropped_img)
    name=""
    if pred.argmax==0:
        name="김승연"
    elif pred.argmax==1:
        name="배유림"
    elif pred.argmax==2:
        name="우민규"
    elif pred.argmax==3:
        name="유길상"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (0, 255, 0)  # 텍스트 색상 (BGR 형식)
    
    cv2.putText(img, name, (10, 50), font, font_scale, text_color, font_thickness)
    
cv2.imshow('Image with Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()