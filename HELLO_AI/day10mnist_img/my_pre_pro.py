import tensorflow as tf
import numpy as np
import cv2
from tensorflow import keras

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

x_text1=x_test[0:1]

img=cv2.imread("9_3.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray_20=cv2.resize(img_gray,(28,28))

x_text1 = np.reshape(img_gray_20,(1,28,28,1)) /255.0

x_text1_Rev=1-x_text1

print(x_text1)

model = tf.keras.models.load_model('first.h5')
model.summary()



pred = model.predict(x_text1_Rev)
print(np.argmax(pred))