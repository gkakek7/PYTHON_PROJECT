import cv2
import numpy as np
from day20face3.my_pred_oop import AiFace
from PIL import ImageFont, ImageDraw, Image


print(cv2.__version__)

image = cv2.imread('team.jpg')
image=cv2.resize(image,(1000,750))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
af=AiFace();
for idx,(x, y, w, h) in enumerate(faces):
    cropped_img = image[y:y+h, x:x+w]
    
    cropped_img=cv2.resize(cropped_img,(32,32))
    myname=af.getNameByImage(cropped_img)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    image = Image.fromarray(image)  
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/gulim.ttc", 12) #글자 사이즈
    draw.text((x, y-20), myname, font=font, fill=(255,255,0))
    
    image = np.array(image) 
    


cv2.imshow('k', image)
cv2.waitKey(0)
cv2.destroyAllWindows()