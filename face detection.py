import numpy as np
import cv2

img = cv2.imread('manyface.png')
img1 = cv2.imread('lenna.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 7)
faceRect1 = faceCascade.detectMultiScale(gray1, 1.1, 7)

print(len(faceRect))
print(len(faceRect1))


for (x, y, w, h) in faceRect:
    cv2.rectangle(img,(x, y),(x+w, y+h),(0, 255, 0), 2)
for (x, y, w, h) in faceRect1:
    cv2.rectangle(img1,(x, y),(x+w, y+h),(0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('img1', img1)

cv2.waitKey(0)