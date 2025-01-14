import cv2
import numpy as np

img = cv2.imread('shape.png')
imgcontour = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 150 ,200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 4)
    #print(cv2.contourArea(cnt))#面積
    area = cv2.contourArea(cnt)
    if area > 100:
        #print(cv2.arcLength(cnt, True))#邊長（圖,是否閉合的圖形）
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri*0.04, True)#多邊形近似輪廓
        print(len(vertices))
        corners = len(vertices)
        x, y, w, h =cv2.boundingRect(vertices)
        cv2.rectangle(imgcontour, (x,y), (x+w, y+h), (0,255,0), 4)
        if corners == 3:
            cv2.putText(imgcontour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
        elif corners == 4:
            cv2.putText(imgcontour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
        elif corners == 5:
            cv2.putText(imgcontour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
        elif corners >= 6:
            cv2.putText(imgcontour, 'cercle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
cv2.imshow('gray', canny)
cv2.imshow('imgcontour', imgcontour)
cv2.waitKey(0)