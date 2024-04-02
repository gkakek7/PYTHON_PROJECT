import cv2

cam = cv2.VideoCapture('sarang.mp4')
while(cam.isOpened()):
    status, frame = cam.read()
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        B = face_region.shape[0]
        S = face_region.shape[1]
        
        face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
        face_region = cv2.resize(face_region, (S, B), interpolation=cv2.INTER_AREA)
        frame[y:y+h, x:x+w] = face_region
    if status:
        cv2.imshow('frame',frame)

    if cv2.waitKey(1)== 113:
        break
    
cam.release()
cv2.destroyAllWindows()