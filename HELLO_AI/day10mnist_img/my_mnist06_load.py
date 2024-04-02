import tensorflow as tf
import numpy as np
import cv2
from tensorflow import keras

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print(x_train.reshape)
# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = tf.keras.models.load_model('first.h5')
model.summary()
# x_train=x_train.reshape((1,28,28,1))
img=cv2.imread("9.jpg",cv2.IMREAD_GRAYSCALE)
img = img.flatten()
img=cv2.resize(img, dsize=(28,28), interpolation=cv2.INTER_LINEAR)
img=img.reshape((1, 28, 28, 1))

pred = model.predict(img)
print(np.argmax(pred))