import cv2

img = cv2.imread("sukgu.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("sukgu",img_gray)
print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()