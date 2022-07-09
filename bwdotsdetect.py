import cv2
from matplotlib.contour import ContourSet

imgray = cv2.imread('pictures/elli.png',0)

_, th = cv2.threshold(imgray, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

contour = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

s1 = 3
s2 = 20
xcnts = []
for cont in contour:
    if s1<cv2.contourArea(cont)<s2 :
        xcnts.append(cont)

print("\nDots number: {}".format(len(xcnts)))
