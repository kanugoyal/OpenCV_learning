import cv2 
print(cv2.__version__)
image = cv2.imread('road.jpg')
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'Hello There',(0,100),font,2,(255,255,255),3) 
 #text,coordinate,font,size of text,color,thickness of font
print(image)
# 1 0 -1
cv2.imwrite('test.jpg',image)
cv2.imshow('eirst image', image)
cv2.waitKey(0)
# cv2.destroyAllWindows() 