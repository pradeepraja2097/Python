import cv2
import numpy as np
img=cv2.imread("tajmahal.jpg")
lr1=cv2.pyrDown(img) #laplacian pyramid it reduces the size
lr2=cv2.pyrDown(lr1)
hr1=cv2.pyrUp(lr2) # it increase the size of the image
cv2.imshow("original image",img)
cv2.imshow("pyrDown",lr1)
cv2.imshow("pyrDown1",lr2)
cv2.imshow("pyrUp",hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()