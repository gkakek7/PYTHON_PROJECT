import tensorflow.keras as keras
import cv2
import numpy as np
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape((-1,28,28,1))/255.0
x_test = x_test.reshape((-1,28,28,1))/255.0

model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(28, 28, 1)), classes=10)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)