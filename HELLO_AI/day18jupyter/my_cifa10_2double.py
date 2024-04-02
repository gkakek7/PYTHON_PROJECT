from time import time
import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

x_train1 = x_train
y_train1 = y_train
x_test1 = x_test
y_test1 = y_test

for i in range(2,20+1):
    x_train = np.append(x_train,x_train1)
    y_train = np.append(y_train,y_train1)
    x_test = np.append(x_test,x_test1)
    y_test = np.append(y_test,y_test1)
    
    x_train = x_train.reshape(-1, 32, 32, 3)
    y_train = y_train.reshape(-1, 1)
    x_test = x_test.reshape(-1, 32, 32, 3)
    y_test = y_test.reshape(-1, 1)
    
    np.save("D:/mnist/x_train{}".format(i),x_train)
    np.save("D:/mnist/y_train{}".format(i),y_train)
    np.save("D:/mnist/x_test{}".format(i),x_test)
    np.save("D:/mnist/y_test{}".format(i),y_test)

