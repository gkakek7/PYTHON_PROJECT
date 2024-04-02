import cv2

img = cv2.imread("gana_eng\GA3_1.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.resize(img_gray,(56,56))
cv2.imshow("sukgu",img_gray)
print(img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()