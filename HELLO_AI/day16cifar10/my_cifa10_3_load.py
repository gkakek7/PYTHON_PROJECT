import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time
import cv2
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = tf.keras.models.load_model('cifa10.h5')

model.summary()
pred = model.predict(x_test)

print(pred.shape)
cnt_o=0;
cnt_n=0;
