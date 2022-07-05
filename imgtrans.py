import cv2
import numpy as np
  
image = cv2.imread('pictures/highway.jpg')
  
height, width = image.shape[:2]
  
half_height, half_width = height / 2, width / 2
  
T = np.float32([[1, 0, half_width], [0, 1, half_height]])
  
img_translation = cv2.warpAffine(image, T, (width, height))
  
cv2.imshow("Originalimage", image)
cv2.imshow('Translation', img_translation)
cv2.waitKey()
  
cv2.destroyAllWindows()