import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time
import cv2

arr = [
    {'lbl':0, 'f':'00', 'n':'김승연'},
    {'lbl':1, 'f':'01', 'n':'배유림'},
    {'lbl':2, 'f':'02', 'n':'우민규'},
    {'lbl':3, 'f':'03', 'n':'유길상'}
]
img=cv2.imread("1.png")
img=img.reshape(-1,32,32,3)/ 255.0

model = tf.keras.models.load_model('face.h5')
model.summary()

preds = model.predict(img)

myidx=np.argmax(preds[0]);

print(arr[myidx]['n'])