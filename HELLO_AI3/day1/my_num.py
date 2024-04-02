import cv2
import os
import numpy as np
arr_eng=["GA","NA","DA","RA","MA",
         "BA","SA","AA","JA","CA"]
list = os.listdir('gana_pre')
x_train = np.array([])
y_train = np.array([])
for f in list:
    label = f[0:2]
    print(label)
    myclass = -1
    if label == "GA": myclass=0
    if label == "NA": myclass=1
    if label == "DA": myclass=2
    if label == "RA": myclass=3
    if label == "MA": myclass=4
    
    if label == "BA": myclass=5
    if label == "SA": myclass=6
    if label == "AA": myclass=7
    if label == "JA": myclass=8
    if label == "CA": myclass=9
    my_np = np.array([myclass])
    y_train=np.concatenate((y_train,my_np))
    

    img = cv2.imread("gana_pre\{}".format(f))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray2 = cv2.resize(img_gray,(56,56))
    img_gray2=np.reshape(img_gray2,(56*56))
    # print(img_gray2)
    x_train = np.concatenate((x_train,img_gray2))



x_train = np.reshape(x_train,(-1,56,56))
print(x_train.shape)
print(y_train.shape)

np.save('x_train.npy',x_train)
np.save('y_train.npy',y_train)

# arr = np.array([1,2,3])
# arr2= np.array([4,5])
# arr= np.concatenate((arr,arr2))
# print(arr)