import cv2 
import numpy as np
print(cv2.__version__)
image1 = cv2.imread('pictures/1bit1.png')
image2 = cv2.imread('pictures/2bit2.png')

dest_and = cv2.bitwise_and(image2,image1,mask=None)

# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(image,'Hello There',(0,100),font,2,(255,255,255),3) 
 #text,coordinate,font,size of text,color,thickness of font
# print(image)
# 1 0 -1
# cv2.imwrite('t.jpg',image)
cv2.imshow('Bitwise And',dest_and)
cv2.waitKey(0) 
# cv2.destroyAllWindows() 