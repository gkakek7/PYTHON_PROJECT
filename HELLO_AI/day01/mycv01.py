import cv2
img = cv2.imread("mask/boy.png")

cv2.imshow("Lena color",img)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()