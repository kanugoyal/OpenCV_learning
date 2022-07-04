import cv2 
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
image = cv2.imread('pictures/highway.jpg')

lr1 = cv2.pyrDown(image)
lr2 = cv2.pyrDown(image)
lr3 = cv2.pyrDown(image)
lr4 = cv2.pyrDown(image)

hr2 = cv2.pyrUp(lr2)

cv2.imshow("Original image", image)
cv2.imshow("pyrdown1", lr1)
cv2.imshow("pyrdown1", lr2)
cv2.imshow("pyrdown1", lr3)
cv2.imshow("pyrdown1", lr4)

cv2.imshow("pyrup", hr2)


cv2.waitKey(0)
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(image,'Hello There',(0,100),font,2,(255,255,255),3) 
 #text,coordinate,font,size of text,color,thickness of font
# print(image)
# 1 0 -1
# cv2.imwrite('t.jpg',image)


# cv2.waitKey(0) 
# cv2.destroyAllWindows() 