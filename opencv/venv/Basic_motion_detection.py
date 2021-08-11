import cv2
import numpy as np

cap=cv2.VideoCapture('vtest.avi')

ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    #  find the difference
    diff=cv2.absdiff(frame1,frame2)
    # convert it into gray scale to find the contour
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    # make it into gaussian blur
    blur=cv2.GaussianBlur(gray,(5,5),0)
    # threshold
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    # Dilation  to fill the holes of the threshold images
    dilated=cv2.dilate(thresh,None,iterations=3)
    # to find the contour
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # to draw the contour
    #cv2.drawContours(frame1,contour,-1,(0,255,0),3)

    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour) <900:
            continue
        cv2.rectangle(frame1,(x,y),(x+w, y+h),(0,255,0),3)
        cv2.putText(frame1,"status :{}".format('movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow("FEED",frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(40)==27:
        break

cv2.destroyAllWindows()



