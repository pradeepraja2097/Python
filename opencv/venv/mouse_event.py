import cv2
import numpy as np

def click_events(event,x,y,flags,param):
    if event== cv2.EVENT_LBUTTONDOWN:#event function
        print(x,',',y)#prints the coordinates vslue
        font=cv2.FONT_HERSHEY_SIMPLEX#font shape
        strXY=str(x)+', ' + str(y)#print the coordinates in the image
        cv2.putText(img,strXY,(x,y),font,0.3,(130,235,45),1)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,-1]
        font = cv2.FONT_HERSHEY_SIMPLEX  # font shape
        strBGR = str(blue) + ', ' + str(green) +','+ str(red) # print the coordinates in the image
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 235, 145), 2)
        cv2.imshow('image', img)

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('messi.jpg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_events)# callback functions

cv2.waitKey(0)
cv2.destroyAllWindows()