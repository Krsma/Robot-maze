import numpy
import cv2





img = cv2.imread('example.jpg')
net=numpy.zeros(shape=(15,15))
matrica=numpy.zeros(shape=(15,15))
img=cv2.resize(img,(150,150),interpolation = cv2.INTER_CUBIC)
#matrica=numpy.matrix(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1:1,0,0,0,1,1,1,1,1,1,1,1,1,1,1:)
def box_value(a,b):
   sum=0
   for i in range((img.shape[0]//15)*a,(img.shape[0]//15)*(a+1)):
       for j in range((img.shape[1]//15)*b,(img.shape[1]//15)*(b+1)):
          px=img[i,j]
          sum=sum+px[0]+px[1]+px[2]
   return sum

def susedni(a,b):
    sum=0
    if b==15:
        rigth=0
    else:
        right = matrica[i,j+1]
    if a==15:
        down=0
    else:
        down=matrica[i+1,j]
    if b==0:
        left=0
    else:
        left=matrica[i,j-1]
    if a==0:
        top=0;
    else:
        top= matrica[i-1,j]
    sum=top+down+left+right
    return sum


for i in range(0,15):
    for j in range(0,15):
        x=img.shape[0]//15*i
        y=img.shape[1]//15*j
        if box_value(i,j)<30000:
            net[i,j]=1
        else:
            net[i,j]=0

for i in range (0,15):
    for j in range(0,15):
        matrica[i,j]=net[i,j]

deleted=1
while deleted>0:
    deleted=0
    for i in range (0,15):
        for j in range(0,15):
            if matrica[i,j]==0:
                 if susedni(i,j)==3:
                    matrica[i,j]=1
                    deleted=deleted+1

for i in range (0,15):
    for j in range(0,15):
        print(matrica[i,j], end=' ')
    print()
