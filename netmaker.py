import cv2
import numpy



img = cv2.imread('example.jpg')
net=numpy.zeros(shape=(10,10))

img=cv2.resize(img,(150,150),interpolation = cv2.INTER_CUBIC)

def box_value(a,b):
   sum=0
   for i in range(img.shape[0]//15*a,img.shape[0]//15*(a+1)):
       for j in range(img.shape[1]//15*b,img.shape[1]//15*(b+1)):
          px=img[i,j]
          sum=sum+px[0]+px[1]+px[2]
   return sum


for i in range(0,img.shape[0]//15):
    for j in range(0,img.shape[1]//15):
        x=img.shape[0]/15*i
        y=img.shape[1]/15*j
        if box_value(i,j)<15000:
            net[i,j]=1
        else:
            net[i,j]=0

for i in range(0,10):
    for j in range(0,10):
        print (net[i,j])
