import tensorflow as tf
import numpy as np
from tensorflow import keras
import cv2

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = tf.keras.models.load_model('fashion.h5')
model.summary()
pred = model.predict(x_test)

for idx, i in enumerate(x_test):
    myidx = np.argmax(pred[idx])
    goog=y_test[idx]
    if myidx!=goog:
        img2=cv2.imwrite("x/{}_{}_{}.jpg".format(idx,myidx,goog),x_test[idx]*255)