import cv2
import numpy as np
from PIL import ImageFont,Image, ImageDraw

img = cv2.imread("dong.jpg")

img=Image.fromarray(img)

draw=ImageDraw.Draw(img);

font =  ImageFont.truetype('font/gulim.ttc',40)
draw.text((300,100),"마동석",font=font,fill=(0,255,0))
img=np.array(img)

cv2.imshow("dong",img)
cv2.waitKey(0)
cv2.destroyAllWindows()