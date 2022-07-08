import cv2
import numpy as np

cap = cv2.VideoCapture(0);

# if (cap.isOpened()):
#     print("Error opening vedio file")
while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    # if ret == True:
    cv2.imshow('Frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()
