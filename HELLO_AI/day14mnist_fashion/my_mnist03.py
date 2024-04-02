import tensorflow as tf
from tensorflow import keras
import cv2

(x_train, y_train), (x_test, y_test) =  tf.keras.datasets.fashion_mnist.load_data()

for idx,t in enumerate(x_train):
    img2=cv2.imwrite("img/{}/{}.png".format(y_train[idx],idx),t)
