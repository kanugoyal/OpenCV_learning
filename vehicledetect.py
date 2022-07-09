import cv2
from cv2 import CV_32SC2

cap = cv2.VideoCapture('video.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 9 )

    for (x, y, w, h) in cars:
        plate = frames[y:y+h, x:x+w]
        cv2.rectangle(frames, (x,y), (x+w, y+h), (51,51,255), 2)
        cv2.rectangle(frames, (x, y-40), (x+w,y), (51,51,255), -1 )
        cv2.putText(frames, 'car', (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,0,0), 1)
        cv2.imshow('car', plate)


       
    cv2.imshow("cars detection", frames)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()