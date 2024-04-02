import cv2

img = cv2.imread("k.png")
# 이미지의 크기를 잡고 이미지의 중심을 계산합니다.
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
 
# 이미지의 중심을 중심으로 이미지를 45도 회전합니다.
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated_45 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("k1",img)
cv2.imshow("k2",rotated_45)


cv2.waitKey(0)
cv2.destroyAllWindows()