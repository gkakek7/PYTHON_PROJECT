import cv2
import os
list = os.listdir('gana_eng')
print(list)
for f in list:
    img = cv2.imread("gana_eng\{}".format(f))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray2 = cv2.resize(img_gray,(56,56))
    cv2.imwrite('gana_pre\{}'.format(f),img_gray2)
    
