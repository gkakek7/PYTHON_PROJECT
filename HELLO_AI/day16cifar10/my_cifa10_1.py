import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from datetime import datetime
import cv2
# airplane : 0
# automobile : 1
# bird : 2
# cat : 3
# deer : 4
# dog : 5
# frog : 6
# horse : 7
# ship : 8
# truck : 9

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

for i in range(1000):
    img2=cv2.imwrite("img/{}/{}.png".format(y_train[i][0],i),x_train[i])
    print(y_train[i])
    
print("x_train.shape",x_train.shape)
print("y_train.shape",y_train.shape)
print("x_test.shape",x_test.shape)
print("y_test.shape",y_test.shape)
