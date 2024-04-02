import cv2

img = cv2.imread("k.png")
x=100
y=100
w=100
h=100
cropped_img = img[y: y + h, x: x + w]

cv2.imshow("k",img)
cv2.imshow("k_crop",cropped_img)


cv2.waitKey(0)
cv2.destroyAllWindows()