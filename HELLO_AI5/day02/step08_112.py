import cv2
import os
def resize112(file_old,file_new):
    img = cv2.imread(file_old)
    x=80
    y=55
    w=497
    h=373
    cropped_img = img[y: y + h, x: x + w]
    
    resize_img = cv2.resize(cropped_img, (28*4,28*4))
    cv2.imwrite(file_new,resize_img)


path = "animal_en_s"
f_list = os.listdir(path)

for idx,fn in enumerate(f_list):
    fsub_list = os.listdir("{}/{}".format(path,fn))
    for idx_s,fs in enumerate(fsub_list):
        file_old = "animal_en_s/{}/{}".format(fn,fs)
        file_new = "animal_en_s112/{}/{}".format(fn,fs)
        resize112(file_old,file_new)
