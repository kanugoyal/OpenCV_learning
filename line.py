import cv2 
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
image = cv2.imread('pictures/highway.jpg')

start_point = (0, 0)
end_point = (250, 250)
color = (0, 255, 0)
thickness = 9

image = cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow("Display", image)

cv2.waitKey(0)



