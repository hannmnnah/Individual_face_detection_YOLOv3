import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640) 
cap.set(4, 480) 
face_detector = cv2.CascadeClassifier('/Users/seogihyun/Desktop/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

# ID 입력
face_id = input('\n USER ID 입력하고 엔터 누르세요 ')  # 1부터 입력

count = 0
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        cv2.imwrite("/Users/seogihyun/Desktop/photo." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff            # 비디오 종료 시 'ESC' 누르기 
    if k == 27:
        break
    elif count >= 200:                     # 200개 이미지 뽑고, 종료하기
         break

cap.release()
cv2.destroyAllWindows()
