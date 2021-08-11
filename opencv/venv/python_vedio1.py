import cv2

cap=cv2.VideoCapture(0)#video cature command
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):

 #cap is variable isOpened is function whether it is opened or not based on that it executes the function
    ret,frame=cap.read()#ret denotes when conditions true and frame is variable name.
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out.write(frame)


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# it converts to gray scale image
    cv2.imshow('frame',gray)# it displays the captured video
    if cv2.waitKey(1) & 0xFF ==ord('q'):#waitKey is used to give the delay function

        break
cap.release()# it release  the screen
out.release()
cv2.destroyAllWindows()#destroys all window