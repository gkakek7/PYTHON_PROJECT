import cv2
import os
import numpy as np
folder_path = 'pre01/'

x_train = []
y_train = []
cnt=0;
for i in os.listdir(folder_path):
    imgs = folder_path + str(cnt)+'/'
    for i in os.listdir(imgs):
        print(imgs+i)
        img = cv2.imread(imgs+i, cv2.IMREAD_COLOR)
        x_train.append(img)
        y_train.append(cnt)
    cnt+=1;
x_train_n = np.array(x_train)
y_train_n = np.array(y_train)
np.save("x_train",x_train_n)
np.save("y_train",y_train_n)
print(x_train_n.shape)
print(y_train_n.shape)