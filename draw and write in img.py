from turtle import back, backward
import cv2
import numpy as np

background = np.zeros((600, 600, 3),np.uint8)

cv2.line(background, (0, 0), (600, 600) ,(255, 255, 255), 2)#（圖片,初始點,終點,顏色,粗度）
#cv2.line(background, (0,0),(background.shape[1],background.shape[0]),(255,255,255),2)

cv2.rectangle(background,(0,0), (400, 300), (0, 255, 255), 1)#畫方形（圖片,方形左上角的點,方形右下角的點,顏色,粗度）
#cv2.rectangle(background,(0,0), (300, 300), (0, 255, 255), cv2.FILLED)#填滿

cv2.circle(background,(300, 300), 100, (255,0,255),1)#畫圓（圖片,圓心,半徑,顏色,粗度,）
#cv2.circle(background,(300, 300), 100, (255,0,255),cv2.FILLED)#填滿 


cv2.putText(background, "julietouo", (100, 500), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,0), 3)#插入文字（圖片,文字,左下角點的座標,字體,大小,顏色,粗度）


cv2.imshow('black', background)
cv2.waitKey(0)