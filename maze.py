import cv2
import numpy

nodes=""
class my_node:
    x_axis=""
    y_axis=""
    left=""
    rigth=""
    top=""
    down=""
    bend=""
    def __init__(self,x_axis,y_axis,bend):
        self.x_axis=x_axis
        self.y_axis=y_axis
        self.bend=bend   #odredjuje da li je node pocetak,kraj ili samo obican node



matrica=numpy.zeros(shape=(1500,1500))
node=numpy.zeros(shape=(1500,1500))
img=cv2.imread('slika.jpg')

def imageanal(img):
    for x in range(0,1500):
        for y in range(0,1500):
            px=img[x,y]
            if px[1]>240 and px[2]>240 and px[3]>240:
                matrica[x,y]=0
            elif px[1]<40 and px[2]<40 and px[3]<40:
                matrica[x,y]=1
    return(matrica)

def define_node():
    for x in range(0,1500):
        for y in range(0,1500):
            if matrica[x,y]==0 and matrica[x+1,y]==1:
                node[x,y]=1
            elif matrica[x,y]==0 and matrica[x,y+1]==0:
                node[x,y]=1
            elif matrica[x,y]==0 and matrica[x-1,y]==1:
                node[x,y]=1
            elif matrica[x,y]==0  and matrica[x,y-1]==0:
                node[x,y]=1
    return(node)

def create_node(x,y,b):
 temp_node=my_node(x,y,b)
 nodes.append(temp_node)

def node_connections():             #uzasan nacin popunjavanja varijabli rltd ali jbg nemam neku mnogo bolju ideju
    for i in range(0,len(list)):
        temp_node=nodes[i]
        for k in range(temp_node.x_axis,1500):
            if node[k,temp_node.y_axis]==1:
                nodes[i].right=k
        for l in range(temp_node.x_axis,0):
            if node[l,temp_node.y_axis]==1:
                nodes[i].left=l
        for j in range(temp_node.y_axis,1500):
            if node[temp_node.x_axis,j]==1:
                nodes[i].down=j
        for h in range(temp_node.y_axis,0):
            if node[temp_node.x_axis,h]==1:
                nodes[i].top=h



