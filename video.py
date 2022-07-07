import cv2
import numpy as np

cap = cv2.VideoCapture('woody.mp4');


# if (cap.isOpened()== False):
#     print("Error opening vedio file")
while(cap.isOpened()):
    ret, frame = cap.read()
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


    if ret == True:
     cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
 
    
cap.release()
cv2.destroyAllWindows()
