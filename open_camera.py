
import cv2 

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)
    else:
        break
    if cv2.waitKey(1) == ord('s'):
        break