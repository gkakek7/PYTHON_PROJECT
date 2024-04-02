import cv2
import os
import numpy as np
list = os.listdir('animal_en_s112')
x_train = np.array([])
y_train = np.array([])
for idx,f in enumerate(list):
    f_list=os.listdir('animal_en_s112/{}'.format(f))
    for fs in f_list:
        my_np = np.array([idx])
        y_train=np.concatenate((y_train,my_np))
        
        file_new="animal_en_s112/{}/{}".format(f,fs)
        img = cv2.imread(file_new)
        print(f,file_new)
        img_flat=np.reshape(img,(112*112*3))
        x_train = np.concatenate((x_train,img_flat))

x_train = np.reshape(x_train,(-1,28*4,28*4,3))
print(x_train.shape)
print(y_train.shape)

np.save('x_train.npy',x_train)
np.save('y_train.npy',y_train)

# arr = np.array([1,2,3])
# arr2= np.array([4,5])
# arr= np.concatenate((arr,arr2))
# print(arr)