import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time
import cv2
x_train=np.load("x_train.npy")
y_train=np.load("y_train.npy")

x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)

model = tf.keras.models.load_model('face.h5')

model.summary()
pred = model.predict(x_train)

for idx,p in enumerate(pred):
    print(idx,np.argmax(p))