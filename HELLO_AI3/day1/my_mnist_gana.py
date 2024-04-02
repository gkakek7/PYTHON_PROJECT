import tensorflow as tf
from tensorflow import keras
import numpy as np

# MNIST 데이터셋 로드
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train=np.load("x_train.npy")
y_train=np.load("y_train.npy")

# 입력 데이터 전처리
x_train = x_train.reshape((-1, 56, 56, 1)) / 255.0

# 모델 구성
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(56,56,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
history = model.fit(x_train, y_train, epochs=20, batch_size=64, validation_split=0.2)

# 모델 평가
test_loss, test_acc = model.evaluate(x_train, y_train)
print('Test accuracy:', test_acc)