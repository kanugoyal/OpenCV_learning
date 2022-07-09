import cv2
import numpy as np
import time

print(cv2.__version__)

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0         #capturing background

for i in range(30):
    ret,background = cap.read()

background = np.flip(background, axis = 1)        #flipping the bg

while True:                          #reading frame in  infinte loop
    ret, image = cap.read()
    image = np.flip(image, axis=1)    #flipping real frame
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  #converting bgr format to hsv format to detect red color
    blur = cv2.GaussianBlur(hsv, (35, 35), 0)     #applyig blur to frame

    lower = np.array([0,120,70])          #defining the lower bound of red color
    upper = np.array([10, 255, 255])       #upperbound of red color

    mask1 = cv2.inRange(hsv, lower,upper)    #creating a mask 

    lower_red = np.array([170,120,70])
    upper_red = np.array([100, 255, 255])

    mask2 = cv2.inRange(hsv, lower_red,upper_red)    
    mask = cv2.addWeighted( mask1, 1, mask2, 2,0)                      #joining the mask

    mask = cv2.morphologyEx(mask , cv2.MORPH_OPEN , np.ones((5,5), np.uint8), iterations = 1)    #using morph operation (erosion+dilation = opening)

    image[np.where(mask== 255)] = background[np.where(mask == 255)]        #converting into background to make invisible


    cv2.imshow("Display", image)
   

    k= cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()