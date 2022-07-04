import numpy as np
import cv2
  

width = 400
height = 300
  
img = np.zeros((height, width, 3), np.uint8)
  
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)
  

cv2.line(img, p1, p2, (255, 0, 0), 3)
cv2.line(img, p2, p3, (255, 0, 0), 3)
cv2.line(img, p1, p3, (255, 0, 0), 3)

centroid = ((p1[0]+p2[0]+p3[0])//3, (p1[1]+p2[1]+p3[1])//3)
  

cv2.circle(img, centroid, 4, (0, 255, 0))
  

cv2.imshow("image", img)
cv2.waitKey(0)