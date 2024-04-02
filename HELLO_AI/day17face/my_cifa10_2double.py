import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(x_train.shape)
arr=x_train

arr_n1 = np.array(arr)
arr_n2 = np.array(arr)

x_train2=np.append(arr_n1,arr_n2)
x_train2=x_train2.reshape(-1,32,32,3)
np.save("x_train2",x_train2)
print(x_train2.shape)