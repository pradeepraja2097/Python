import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('img.png')  #opencv reads in bgr format
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #matplotlib reads in rgb


kernel=np.ones((5,5),np.float32)/25 #based on pixel format it works on homogenous filter
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5));
gblur=cv2.GaussianBlur(img,(5,5),0) # gaussian blur the weightage of the pixel is different in different area
median=cv2.medianBlur(img,5)#median filter is somthing to replace each pixel value with its neighbour pixels

titles=['image','2D convolution','blur','gblur','medain' ]
images=[img,dst,blur,gblur,median]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()