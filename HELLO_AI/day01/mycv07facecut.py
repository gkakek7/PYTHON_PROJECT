import cv2

print(cv2.__version__)

image = cv2.imread('k.png')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for idx,(x, y, w, h) in enumerate(faces):
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face_img = image[y:y+h, x:x+w]
    cv2.imwrite("{}.png".format(idx), face_img)


cv2.imshow('k', image)

cv2.waitKey(0)
cv2.destroyAllWindows()