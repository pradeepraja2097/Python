import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((5,5),np.uint8)# it is square shape structure to mask it up the noise

dilation=cv2.dilate(mask,kernal,iterations=2)
erosion=cv2.erode(mask,kernal,iterations=2)     #errosion means it erodes the boundary
opening =cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)   #first errosion happens and dilation occurs
closing =cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)  #first dilation happens and errosions occurs
mg =cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)    #difference between dilation and eroosions
tophat =cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
titles=['image','mask','dilation','erosions','opening','closing','mg','tophat']
images=[img,mask,dilation,erosion,opening,closing,mg,tophat]


for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.show()