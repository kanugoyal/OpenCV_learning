from tracemalloc import start
import cv2 
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
image = cv2.imread('pictures/highway.jpg')

start_point=(20,20)
end_point = (220,220)
color = (255, 0, 0)
thickness = 5

image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("Rectangle", image)
cv2.waitKey(0)



