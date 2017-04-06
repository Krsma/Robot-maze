import cv2    #python ima probel sa bibliotekama, na mom kompjuter prijavljuje gresku
import numpy


nodes=""
centering_list=""
class my_node:
    x_axis=""
    y_axis=""
    left=""        #veze sa drugim nodeovima
    rigth=""
    top=""
    down=""
    bend=""
    connection=""       #ovo i prev_connection se koriste kao koneckicije sa odeovima na putu ka kraju
    prev_connection=""
    def __init__(self,x_axis,y_axis,bend):
        self.x_axis=x_axis
        self.y_axis=y_axis
        self.bend=bend   #odredjuje da li je node pocetak,kraj ili samo obican node

class centering_points:
    posx=""
    posy=""
    def __init__(self,posx,posy):
        self.posx=posx
        self.posy=posy



matrica=numpy.zeros(shape=(1500,1500))
node=numpy.zeros(shape=(1500,1500))
for_centering=numpy.zeroes(shape=(1500,1500))
#lavirint=numpy.zeros(shape=(1500,1500))
img=cv2.imread('slika.jpg')        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#geometric-transformations

def imageanal(img):
    for x in range(0,1500):
        for y in range(0,1500):
            px=img[x,y]
            if px[1]>240 and px[2]>240 and px[3]>240:
                matrica[x,y]=0          #0 za put
            elif px[1]<40 and px[2]<40 and px[3]<40:
                matrica[x,y]=1          #1 za put
            elif px[1]<40 and px[2]>200 and px[3]>200:
                node[x,y]=2        #2 za start
            elif px[1]>200 and px[2]>200 and px[3]<40:
                node[x,y]=3          #3 za end
    return(matrica)

def image_imagecenter():                 #centriranje slike pomocu crvenih tacaka na slici
    for x in range(0,1500):
        for y in range(0,1500):
            px=img[x,y]
            if px[1]>200 and px[2]<50 and px[3]<50:
                temp=centering_points(x,y)
                centering_list.append(temp)
    pts1 = np.float32([[centering_list[1].posx, centering_list[1].posy], [centering_list[2].posx, centering_list[2].posy], [centering_list[3].posx, centering_list[3].posy], [centering_list[4].posx, centering_list[4].posy]])
    pts2 = np.float32([[0, 0], [1500, 0], [0, 1500], [1500, 1500]])   #kod kopiran sa sajta opencv
    M = cv2.getPerspectiveTransform(pts1, pts2)                       #problem je verovatno sa numpy bibliotekom

    dst = cv2.warpPerspective(img, M, (300, 300))


def define_node():                 #posle analize slike odrediti nodeove
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

def fill_list():
    for i in range(0,1500):
        for f in range(0,1500):
            if node[i,f]==1:
                px=img[i,f]

                if px[1]<40 and px[2]>200 and px[3]>200:
                    create_node(i,f,1)
                elif px[1] > 200 and px[2] > 200 and px[3] < 40:
                    create_node(i,f,2)
                else:
                    create_node(i,f,0)



def node_connections():             #uzasan nacin popunjavanja varijabli rltd ali jbg nemam neku mnogo bolju ideju
    for i in range(0,len(nodes)):
        temp_node=nodes[i]
        for k in range(temp_node.x_axis,1500):
            if node[k,temp_node.y_axis]==1:
                nodes[i].right=k
                break
        for l in range(temp_node.x_axis,0):
            if node[l,temp_node.y_axis]==1:
                nodes[i].left=l
                break
        for j in range(temp_node.y_axis,1500):
            if node[temp_node.x_axis,j]==1:
                nodes[i].down=j
                break
        for h in range(temp_node.y_axis,0):
            if node[temp_node.x_axis,h]==1:
                nodes[i].top=h
                break


#procedure za resavanje lavirinta

