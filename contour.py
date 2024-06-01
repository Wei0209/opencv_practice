import cv2
import numpy as np

img = cv2.imread("shape.png")
cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([35, 50, 50])
upper = np.array([85, 255, 255])  

mask = cv2.inRange(cvt, lower, upper)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
    contour = contours[0]
    area = cv2.contourArea(contour)
    print("面積:", area)
else:
    print("未找到任何轮廓")

cv2.imshow('Image', img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
