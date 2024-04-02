import tensorflow as tf
from tensorflow import keras
import numpy as np

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

# print(x_train.shape)
# print(y_train.shape)

# 입력 데이터 전처리
x_train = x_train/ 255.0

model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(112, 112, 3)), classes=5)

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=5)
model.save('animal.h5')