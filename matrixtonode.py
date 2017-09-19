import cv2
import numpy
from operator import xor

img = cv2.imread('test2green.jpg')
net=numpy.zeros(shape=(15,15))
nodelist = []

class node(object):
    north = 0
    south = 0
    west = 0
    east = 0
    tag = 0
    positionx = 0
    positiony = 0
    def __init__(self,positionx,positiony):
        self.positiony=positiony
        self.positionx=positionx


def box_value(a,b):  #part of netmaker.py code
   green=0
   sum=0
   for i in range((img.shape[0]//15)*a,(img.shape[0]//15)*(a+1)):
       for j in range((img.shape[1]//15)*b,(img.shape[1]//15)*(b+1)):
          px=img[i,j]
          sum=sum+px[0]+px[1]+px[2]
          if (px[1]>200) and (px[0]<100) and (px[2]<100):
              green=green+1

   if green > 50:
        sum=1

   return sum


for i in range(0,15):
    for j in range(0,15):
        x=img.shape[0]//15*i
        y=img.shape[1]//15*j
        if box_value(i,j)==1:
            net[i,j]=2
        elif box_value(i,j)<30000:
            net[i,j]=1
        else:
            net[i,j]=0




for k in range(0,14):   #should be changed to 0..14 and the 15 line is used as an edge
    for f in range(0,14):
        if net[k,f]==0:
            a=(net[k,f+1]==1)
            b=(net[k,f-1]==1)
            c=(net[k+1,f]==1)
            d=(net[k-1,f]==1)
            if ((a and not b) or (b and not a)) or ((c and not d) or (d and not c)):
                x = node(k,f)
                print(k)
                print(f)
                print()
                nodelist.append(x)
