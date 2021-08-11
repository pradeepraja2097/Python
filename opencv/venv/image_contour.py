# contour is nothing but connecting outer boundaries with same colour and same intensity
# it is used for object detection

import cv2
import numpy as np

img=cv2.imread('opencv-logo.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # convert imge to grayscale
ret,thresh=cv2.threshold(imgray,127,255,0) # define the threshold value of imgray image
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  # cv2.CHAIN_APPROX_NONE all the boundary points are storedall the boundary points are stored
# contour  is x,y coordinates of boundary points of the object

print("number of contours =",str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow('image',img)
cv2.imshow('image gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()