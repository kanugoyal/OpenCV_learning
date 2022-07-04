from tracemalloc import start
import cv2 
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
image = cv2.imread('pictures/highway.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50,50)
fontScale = 1
color = (255, 0, 0)
thickness = 5

image = cv2.putText(image, 'OpenCV', org, font, fontScale,  color, thickness)
cv2.imshow("Text", image)
cv2.waitKey(0)



