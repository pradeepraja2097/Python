import cv2
import numpy as np

img=cv2.imread('triangle.png')
imgrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(imgrey,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    # "cv2.approxPolyDP" is to identify the shape by connecting contour
    # cv2.arcLength() is used to calculate the perimeter of the contour.
    # If the second argument is True then it considers the contour to be closed.
    # Then this perimeter is used to calculate the epsilon value for
    # cv2.approxPolyDP() function with a precision factor for approximating a shape.
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx) ==3:
        cv2.putText(img,"TRIANGLE",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio >=0.95 and aspectratio <= 1.05:
            cv2.putText(img, "SQUARE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
        else:
            cv2.putText(img, "RECTANGLE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

    elif len(approx)==5:
        cv2.putText(img, "PENTAGON", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

    elif len(appox)==10:
        cv2.putText(img, "STAR", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

    else:
        cv2.putText(img, "CIRCLE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))


cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
