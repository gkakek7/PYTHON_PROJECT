import cv2

img = cv2.imread("sukgu.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
for (x, y, w, h) in faces:
    face_region = img[y:y+h, x:x+w]
    B = face_region.shape[0]
    S = face_region.shape[1]
    
    face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
    face_region = cv2.resize(face_region, (S, B), interpolation=cv2.INTER_AREA)
    img[y:y+h, x:x+w] = face_region
    
cv2.imshow("sukgu",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
