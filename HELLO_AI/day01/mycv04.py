import cv2

img = cv2.imread("sukgu.jpg")
imageRectangle = img.copy()
cv2.rectangle(imageRectangle, 
            (420,100,350,400),
            (0,255,255), 2) 
cv2.imshow("image", imageRectangle) 

# cv2.imshow("sukgu",img)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()