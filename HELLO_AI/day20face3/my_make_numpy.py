import os
import cv2
import numpy as np
arr = [
    {'lbl':0, 'f':'00', 'n':'김승연'},
    {'lbl':1, 'f':'01', 'n':'배유림'},
    {'lbl':2, 'f':'02', 'n':'우민규'},
    {'lbl':3, 'f':'03', 'n':'유길상'}
]

x_train=np.array([])
y_train=np.array([])

for idxx,a in enumerate(arr):
    files=os.listdir('pre01/{}'.format(a['f']))
    for idx,fn in enumerate(files):
        print(idxx,idx,fn)
        img = cv2.imread("pre01/{}/{}".format(a['f'],fn))
        x_train=np.append(x_train, img)
        y_train=np.append(y_train, np.array([a['lbl']]))

x_train=np.reshape(x_train,(-1,32,32,3))
y_train=np.reshape(y_train,(-1,1))
np.save("x_train",x_train)
np.save("y_train",y_train)
print("x_train.shape",x_train.shape)
print("y_train.shape",y_train.shape)

