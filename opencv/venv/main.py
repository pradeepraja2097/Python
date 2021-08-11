import cv2

img=cv2.imread('tajmahal.jpg',1)


img=cv2.imread('tajmahal.jpg',1)
img=cv2.line(img,(0,0),(50,50),(0,0,255),5)
img=cv2.arrowedLine(img,(0,0),(50,50),(0,0,255),5)
img=cv2.rectangle(img,(150,0),(220,130),(0,255,0),5)
img=cv2.circle(img,(252,130),(63),(0,0,255),5)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'TAJMAHAL',(25,25),font,1,(133,100,90),2)
print(img)
window='image1'
cv2.imshow(window,img)

k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):

    cv2.imwrite('tajmahal_copy.jpg', img)
    cv2.destroyAllWindows()

print(img)
window='image1'
cv2.imshow(window,img)

k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):

    cv2.imwrite('tajmahal_copy.jpg', img)
    cv2.destroyAllWindows()