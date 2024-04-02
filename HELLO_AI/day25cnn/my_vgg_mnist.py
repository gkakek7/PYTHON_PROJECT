import tensorflow.keras as keras
from tensorflow.keras import layers, models
import cv2
import numpy as np
from keras.applications.vgg16 import VGG16
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape((-1,28,28,1))/255.0
x_test = x_test.reshape((-1,28,28,1))/255.0

model = VGG16(weights=None, include_top=False, input_shape=x_train[0].shape)
model.compile(loss=keras.losses.SparseCategoricalCrossentropy(),
          optimizer=keras.optimizers.legacy.Adam(),
          metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)