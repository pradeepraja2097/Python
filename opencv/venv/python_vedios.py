import cv2

cap=cv2.VideoCapture(0)#video cature command

while(True):
    ret,frame=cap.read()#ret denotes when conditions true and frame is variable name.
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# it converts to gray scale image
    cv2.imshow('frame',gray)# it displays the captured video
    if cv2.waitKey(1) & 0xFF ==ord('q'):#waitKey is used to give the delay function

        break
cap.release()# it release  the screen
cv2.destroyAllWindows()#destroys all window

