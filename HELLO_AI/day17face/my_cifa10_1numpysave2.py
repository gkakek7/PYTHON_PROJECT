import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time


arr_n1=np.load("x_train.npy")
arr_n2=np.load("x_train.npy")
np.save("x_train2",np.concatenate([arr_n1, arr_n2], 0))
print(np.concatenate([arr_n1, arr_n2], 0).shape)