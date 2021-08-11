import cv2
import numpy as np

img1=np.zeros((776,1472,3),np.uint8)
#img=cv2.imread('image.png')
#print(img.size)
#print(img.shape)
#print(img.dtype)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread("image.png")
bitXor=cv2.bitwise_xor(img2,img1)

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('bitAnd',bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()