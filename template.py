import cv2
import numpy as np
 
image = cv2.imread('picture/smile.jpg')
 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
template = cv2.imread('template',0)
 
w, h = template.shape[::-1]
 
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
 
threshold = 0.8
 
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
 

cv2.imshow('Detected',image)