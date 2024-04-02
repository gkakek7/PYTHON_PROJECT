import cv2
import os
files = os.listdir('img')
arr = [
    {'lbl':'0', 'f':'01', 'n':'김승연'},
    {'lbl':'1', 'f':'02', 'n':'배유림'},
    {'lbl':'2', 'f':'03', 'n':'우민규'},
    {'lbl':'3', 'f':'04', 'n':'유길상'}
    ]


def mp4Toimg(myname, folder_name):
    cap = cv2.VideoCapture('img/{}.mp4'.format(myname))
    cnt = 0;
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
            for idx,(x, y, w, h) in enumerate(faces):
                cropped_img=frame[y:y+h,x:x+w]
                cropped_img = cv2.resize(cropped_img, dsize=(32, 32))
                cv2.imwrite('pre01/{}/{}.png'.format(folder_name, cnt), cropped_img)
                cnt += 1
        else:
            break


for a in arr:
    mp4Toimg(a['n'], a['f'])
