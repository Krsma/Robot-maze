import cv2
import numpy


img = cv2.imread('lavirinttesst.jpg') #init for the image
net=numpy.zeros(shape=(15,15))
nodelist = []

class node(object):
    north = 0
    south = 0
    west = 0
    east = 0
    tag = 0   #tag will be used as a marker for which node is finall and where the ball starts
    positionx = 0
    positiony = 0
    def __init__(self,positionx,positiony):
        self.positiony=positiony
        self.positionx=positionx

    def connect(self):              #making connections to other nodes, there probably is a better way to do this
        for i in range(positiony,15):
            if net[self.positionx,i]==4:
                self.east=i
            elif net[self.positionx,i]==1:
                break
        for i in range(1,positiony):   #edge is always 1 so we skip that one
            if net[self.positionx,i]==4:
                self.west=i
            elif net[self.positionx,i]==1:
                break

        for j in range(positionx,15):
            if net[j,positiony]==4:
                self.south=j
            elif net[j,positiony]==1:
                break

        for j in range(1,positionx):  #evading the edge
            if net[j,positiony]==4:
                self.north=j
            elif net[j,positiony]==1:
                break







def box_value(a,b):  #part of netmaker.py code
   green=0
   sum=0
   for i in range((150//15)*a,(150//15)*(a+1)):
       for j in range((150//15)*b,(150//15)*(b+1)):
          px=img[i,j]
          sum=sum+px[0]+px[1]+px[2]
          if (px[1]>200) and (px[0]<100) and (px[2]<100):
              green=green+1

   if green > 50:   #this value has to be tweaked based on the actuall image #todo
        sum=1

   return sum


for i in range(0,15):
    for j in range(0,15):
        x=150//15*i
        y=150//15*j
        if box_value(i,j)==1:
            net[i,j]=2     #tag 2 is for start
        elif box_value(i,j)<30000:
            net[i,j]=1     #tag 1 is for wall
        else:
            net[i,j]=0     #tag 0 is for path




for k in range(0,14):   #should be changed to 0..14 and the 15 line is used as an edge
    for f in range(0,14):
        if not(net[k,f]==1):
            a=(net[k,f+1]==1)
            b=(net[k,f-1]==1)
            c=(net[k+1,f]==1)
            d=(net[k-1,f]==1)
            if ((a and not b) or (b and not a)) or ((c and not d) or (d and not c)):
                #i slightly changed this algortihm
                #https://youtu.be/rop0W4QDOUI?t=7m56s
                x = node(k,f)
                print(k)
                print(f)
                print()
                net[k,f]=4 #tag 4 represents that this field contains the node
                nodelist.append(x)

for j in range(0,len(nodelist)):  #go through all nodes you found
        nodelist[j].connect
