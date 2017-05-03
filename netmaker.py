import cv2
import numpy



img = cv2.imread('example.jpg')
net=numpy.zeros(shape=(15,15))

img=cv2.resize(img,(150,150),interpolation = cv2.INTER_CUBIC)

def box_value(a,b):
   sum=0
   for i in range((img.shape[0]//15)*a,(img.shape[0]//15)*(a+1)):
       for j in range((img.shape[1]//15)*b,(img.shape[1]//15)*(b+1)):
          px=img[i,j]
          sum=sum+px[0]+px[1]+px[2]
   return sum


for i in range(0,15):
    for j in range(0,15):
        x=img.shape[0]//15*i
        y=img.shape[1]//15*j
        if box_value(i,j)<30000:
            net[i,j]=1
        else:
            net[i,j]=0

for i in range(0,15):
    for j in range(0,15):
        print (net[i,j])
cv2.imshow("slika", img)
cv2.waitKey(0)
