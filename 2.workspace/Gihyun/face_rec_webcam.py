import cv2
import numpy as np
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

blur = False
framed = False

while True:
    ret, frame = cap.read()
    if(ret):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        f = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        for x,y,w,h in f:
            if blur:
                sub_face = frame[y:y+h, x:x+w]
                sub_face = cv2.GaussianBlur(sub_face, (23,23), 30)
                frame[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

            if framed:
                cv2.rectangle(frame, (x,y), (x+h,y+w), (0,255,0),2)

        cv2.imshow('Face Recognized', frame)

    ch = 0xFF&cv2.waitKey(1)

    if ch == ord('b'):
        blur = not blur
    
    if ch == ord('f'):
        framed = not framed

    if ch == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
