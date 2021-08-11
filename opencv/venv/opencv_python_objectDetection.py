import cv2
import numpy as np
def nothing(x):
    pass
while True:
    frame=cv2.imread('smarties.png')
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_b=np.array([110,50,50])
    u_b=np.array([130,100,100])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask", frame)
    cv2.imshow("res", frame)
    key=cv2.waitKey(1)

    if key==27:
        break

cv2.destroyAllWindows()