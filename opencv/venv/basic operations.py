import cv2
import numpy as np

img = cv2.imread('messi.jpg')
img2=cv2.imread('opencv.png')
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
ball=img[164:165, 203:188]
img[68:69,93:88]=ball
img=cv2.resize(img,(512,512))
img2=cv2.resize(img,(512,512))
#dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,.3,img2,.9,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()