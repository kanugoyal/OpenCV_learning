import cv2 
print(cv2.__version__)
image = cv2.imread('road.jpg')
print(image)
# 1 0 -1
cv2.imwrite('test.jpg',image)
cv2.imshow('eirst image', image)
cv2.waitKey(0)
# cv2.destroyAllWindows() 