import numpy as np
from keras.utils import np_utils
import tensorflow.keras as keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time
x_train=np.load("x_train.npy")
y_train=np.load("y_train.npy")
x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(32, 32, 3)), classes=4)



model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

hist = model.fit(x_train, y_train,
                 epochs=14,
                 batch_size=32,
                )
model.save('face.h5')
