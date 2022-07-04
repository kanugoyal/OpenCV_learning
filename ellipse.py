import cv2 
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
image = cv2.imread('pictures/highway.jpg')

centre_coordinates = (120, 100)
axesLength = (100,50)
angle = 0
startAngle = 0
endAngle = 360
color = (255, 0, 0)
thickness = 8

image = cv2.ellipse(image, centre_coordinates, axesLength,angle, startAngle, endAngle, color, thickness)
cv2.imshow("Ellipse", image)
cv2.waitKey(0)



