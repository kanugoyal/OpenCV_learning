import numpy as np
import cv2
image = cv2.imread('pictures/smile.jpg')

print(image.shape)
print(image.size)
print(image.dtype)
b,g,r = cv2.split(image)
image = cv2.merge((b,g,r))

# face = image[160:180, 200:250]
# image[273:333, 100:160] = face
# image = cv2.resize(image, (512, 512))

# (rows, cols) = image.shape[:2]
R = cv2.getRotationMatrix2D((512, 512), 90, 1)
res = cv2.warpAffine(image, R, (512,512))


cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
