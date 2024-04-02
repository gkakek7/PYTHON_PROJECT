import os
import cv2
import numpy as np
arr_eng=["GA","NA","DA","RA","MA",
         "BA","SA","AA","JA","CA"]
string="가나다라마바사아가자차"
file_path = 'gana_pre'
list = os.listdir(file_path)
x_train=np.array([])
arr=[]
for f in list:
    img = cv2.imread(file_path+"/"+f)
    arr.append(img)

print(arr)    