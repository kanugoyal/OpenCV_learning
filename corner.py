import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('pictures/corner.png')
  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
  
corners = np.int0(corners)
  
for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (x, y), 3, (255, 0, 0), -1)
  
cv2.imshow("corners", image)

   
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()