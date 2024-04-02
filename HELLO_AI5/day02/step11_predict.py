import tensorflow as tf
from tensorflow import keras
import numpy as np

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

model=tf.keras.models.load_model('animal.h5')

pred = model.predict(x_train)
print(pred)
idx1=np.argmax(pred[900][0])
print(np.argmax(pred[900][0]))
idx2=np.argmax(pred[900][idx1])
print(idx2)
idx3=np.argmax(pred[900][idx2])
print(idx3)