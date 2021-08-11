import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("messi.jpg",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=1) # Laplacian filter
lap=np.uint8(np.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0 )# It indicates in x directions
sobely=cv2.Sobel(img,cv2.CV_64F,0,1) # It indicates in y direction
edges=cv2.Canny(img,50,200) # it is used for edge detection and reduce the noises in the image


sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
sobelCombined=cv2.bitwise_or(sobelx,sobely)


title=['image','Laplacian','sobelx','sobely','sobelCombined','canny']
images=[img,lap,sobelx,sobely,sobelCombined,edges]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])

plt.show()