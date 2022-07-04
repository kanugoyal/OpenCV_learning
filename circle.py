import cv2 
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
image = cv2.imread('pictures/highway.jpg')

centre_coordinates = (170, 100)
radius = 40
color = (255, 0, 0)
thickness = -1

image = cv2.circle(image, centre_coordinates, radius, color, thickness)
cv2.imshow("Circle", image)
cv2.waitKey(0)



