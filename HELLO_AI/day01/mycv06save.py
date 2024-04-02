import cv2

img = cv2.imread("sukgu.jpg")
img2=cv2.imwrite("suckgu.png",img)

cv2.imshow("Lena color",img)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()