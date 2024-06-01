import cv2
import numpy as np

kernal = np.ones((5, 5),(np.uint8))
kernal2 = np.ones((5, 5),(np.uint8))

dog = cv2.imread('dog.jpg')
dog = cv2.resize(dog , (0,0), fx = 1.5, fy = 1.5)


gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)#轉灰階
blur = cv2.GaussianBlur(dog,[9, 9], 10)#高斯模糊（要處理的圖片,和的大小[3,3]or[5,5]要奇數,標準差）
canny = cv2.Canny(dog, 100, 200)#找邊緣（要處理的圖片,最低門檻值,最高門檻值)
dilate = cv2.dilate(canny, kernal, iterations=1)#膨脹(處理ㄉ照片（可能是邊緣線條）,kernal,膨脹次數iterations迭代)
erode = cv2.erode(dilate, kernal2, iterations=1)#侵蝕(處理ㄉ照片（可能是邊緣線條）,kernal,膨脹次數iterations迭代)


cv2.imshow('原圖', dog)
cv2.imshow('灰階', gray)
cv2.imshow('模糊', blur)
cv2.imshow('邊緣', canny)
cv2.imshow('膨脹', dilate)
cv2.imshow('侵蝕', erode)

cv2.waitKey(0)