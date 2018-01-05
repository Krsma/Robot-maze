from netmaker import buildnet, readImage, Tag
from valuechecker import check_connect_all,check_buildnet,check_img,checklist

class Node(object):
    north = None
    south = None
    west = None
    east = None
    tag = Tag.PATH  # tag 5 is the final of the maze, tag 2 for the start, tag 1 for regular nodes
    positionx = 0
    positiony = 0
    beenhere = False

    def __init__(self, positionx, positiony, tag):
        self.positiony = positiony
        self.positionx = positionx
        self.tag = tag

    def __str__(self):
        return str(self.tag)
    
    def __repr__(self):
        return str(self.tag)

    def connect(self, nodelist):  # making connections to other nodes, there probably is a better way to do this

        x = self.positionx
        y = self.positiony
        
        self.north = find_node(nodelist, x - 1, y)
        self.south = find_node(nodelist, x + 1, y)
        self.west = find_node(nodelist, x, y - 1)
        self.east = find_node(nodelist, x, y + 1)

def solvethemaze(path):
    if len(path) == 0:
        print("List is empty")
        return
    current = path[- 1]  # take last node

    if current.tag == Tag.FINAL:
        return (path)

    if not (current.east == None):
        if (current.east.tag == Tag.FINAL):
            print("found the end")
            path.append(current.east)
            return (path)

        elif ((current.east.tag == Tag.PATH) and (current.east.beenhere == False)):
            current.beenhere = True
            path.append(current.east)
            return (solvethemaze(path))

    if not (current.west == None):
        if (current.west.tag == Tag.FINAL):
            print("found the end")
            path.append(current.west)
            return (path)

        elif ((current.west.tag == Tag.PATH) and (current.west.beenhere == False)):
            current.beenhere = True
            path.append(current.west)
            return (solvethemaze(path))

    if not (current.north == None):
        if (current.north.tag == Tag.FINAL):
            path.append(current.north)
            print("found the end")
            return (path)

        elif ((current.north.tag == Tag.PATH) and (current.north.beenhere == False)):
            current.beenhere = True
            path.append(current.north)
            return (solvethemaze(path))

    if not (current.south == None):
        if (current.south.tag == Tag.FINAL):
            path.append(current.south)
            print("found the end")
            return (path)

        elif ((current.south.tag == Tag.PATH) and (current.south.beenhere == False)):
            current.beenhere = True
            path.append(current.south)
            return (solvethemaze(path))

def find_node(nodelist, x, y):
    for n in nodelist:
        if n.positionx == x and n.positiony == y:
            return n

def create_nodelist(net):
    nodelist = []
    for k in range(0, 14):  # should be changed to 0..14 and the 15 line is used as an edge
        for f in range(0, 14):
            if not (net[k, f] == Tag.WALL):
                if net[k, f] == Tag.FINAL:
                    x = Node(k, f, Tag.FINAL)
                elif net[k, f] == Tag.START:
                    x = Node(k, f, Tag.START)
                else:
                    x = Node(k, f, Tag.PATH)  # add tag giving into init

                nodelist.append(x)
    return nodelist

def connect_all(path, nodelist):
    for j in range(0, len(nodelist)):  # go through all nodes you found and connect them
        nodelist[j].connect(nodelist)
        if nodelist[j].tag == Tag.START:
            path.append(nodelist[j])

def main():
    img = readImage("lavirinttesst.jpg")
    if check_img(img) == False:
        return


    path = []

    net = buildnet(img)
    if check_buildnet(net) == False:
        return

    nodelist = create_nodelist(net)
    if checklist(nodelist) == False:
        return

    connect_all(path, nodelist)
    if check_connect_all(nodelist) == False:
        return

    print(path)

    solution = solvethemaze(path)
    if checklist(solution) == False:
        return
    print(solution)

if __name__ == "__main__":
    main()
