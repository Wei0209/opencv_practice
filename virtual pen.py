import cv2
import numpy as np
cap = cv2.VideoCapture(0)

colorhsv = [[110,43,46,124,255,255],[0,100,119,179,255,255],[0,0,39,180,37,100]]#藍紅黑0 179 0 37 39 100
colorbgr = [[255,0,0],[0,0,255],[0,0,0]]
drawpoint = []

def findpen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(len(colorhsv)):   
        lower = np.array(colorhsv[i][:3])
        upper = np.array(colorhsv[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        penx, peny = findcontour(mask)
        cv2.circle(imgcontour, (penx, peny), 10, colorbgr[i],cv2.FILLED)
        if peny!= -1:
            drawpoint.append([penx, peny ,i])
    #cv2.imshow('result', result)

def findcontour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1

    for cnt in contours:
        # cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 4)
        area = cv2.contourArea(cnt)
        if area > 300:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True)#多邊形近似輪廓
            x, y, w, h =cv2.boundingRect(vertices)
    return x+w//2 ,y 

def draw(drawpoint):
    for point in drawpoint:
        cv2.circle(imgcontour,(point[0], point[1]), 10, colorbgr[point[2]], cv2.FILLED)

while(1):
    ret ,frame = cap.read()
    if ret:
        imgcontour = frame.copy()
        #cv2.imshow('video', frame)
        findpen(frame)
        draw(drawpoint)
        cv2.imshow('contour', imgcontour)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break