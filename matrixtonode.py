from netmaker import buildnet, readImage, Tag

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

    def connect(self, net, nodelist):  # making connections to other nodes, there probably is a better way to do this
        for i in range(self.positiony, 15):
            if net[self.positionx, i] == Tag.HAS_NODE:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positiony == i) and (nodelist[j].positionx == self.positionx):
                        self.east = nodelist[j]
                        break

            elif net[self.positionx, i] == Tag.WALL:
                break


        for i in range(1, self.positiony):  # edge is always 1 so we skip that one
            if net[self.positionx, i] == Tag.HAS_NODE:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positiony == i) and (nodelist[j].positionx == self.positionx):
                        self.west = nodelist[j]
                        break

            elif net[self.positionx, i] == Tag.WALL:
                break


        for j in range(self.positionx, 15):
            if net[j, self.positiony] == Tag.HAS_NODE:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positionx == i) and (nodelist[j].positiony == self.positiony):
                        self.south = nodelist[j]
                        break

            elif net[j, self.positiony] == Tag.WALL:
                break

        for j in range(1, self.positionx):  # evading the edge
            if net[j, self.positiony] == Tag.HAS_NODE:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positionx == i) and (nodelist[j].positiony == self.positiony):
                        self.north = nodelist[j]
                        break

            elif net[j, self.positiony] == Tag.WALL:
                break

def solvethemaze(nodm):
    if len(nodm) == 0:
        print("List is empty")
        return
    current = nodm[len(nodm) - 1]  # take last node


    if not(current.east == None):
        if (current.east.tag == Tag.FINAL):
            nodm.append(current.east)
            return(nodm)

        elif (not(current.east.tag == Tag.FINAL) and (current.east.beenhere == False)):
            current.beenhere = True
            nodm.append(current.east)
            solvethemaze(nodm)

    if not(current.west == None):
        if (current.west.tag == Tag.FINAL):
            nodm.append(current.west)
            return(nodm)
        
        elif (not(current.west.tag == Tag.FINAL) and (current.west.beenhere == False)):
            current.beenhere = True
            nodm.append(current.west)
            solvethemaze(nodm)

    if not(current.north == None):
        if (current.north.tag == Tag.FINAL):
            nodm.append(current.north)
            return(nodm)

        elif(not(current.north.tag == Tag.FINAL) and (current.north.beenhere == False)):
            current.beenhere = True
            nodm.append(current.north)
            solvethemaze(nodm)
    
    if not(current.south == None):
        if (current.south.tag == Tag.FINAL):
            nodm.append(current.south)
            return(nodm)

        elif(not(current.south.tag == Tag.FINAL) and (current.south.beenhere == False)):
            current.beenhere = True
            nodm.append(current.south)
            solvethemaze(nodm)

def main():
    img = readImage("lavirinttesst.jpg")
    if(img is None):
        return

    nodelist = []
    initstack = []

    net = buildnet(img)

    for k in range(0, 14):  # should be changed to 0..14 and the 15 line is used as an edge
        for f in range(0, 14):
            if not(net[k, f] == Tag.WALL):
                a = (net[k, f + 1] == Tag.WALL)
                b = (net[k, f - 1] == Tag.WALL)
                c = (net[k + 1, f] == Tag.WALL)
                d = (net[k - 1, f] == Tag.WALL)
                if (((a and not b) or (b and not a)) or ((c and not d) or (d and not c))) or (net[k, f] == Tag.FINAL) or (net[k, f] == Tag.START):
                    # i slightly changed this algorithm
                    # https://youtu.be/rop0W4QDOUI?t=7m56s
                    if net[k, f] == Tag.FINAL:
                        x = Node(k, f, Tag.FINAL)
                    elif net[k, f] == Tag.START:
                        x = Node(k, f, Tag.START)
                    else:
                        x = Node(k, f, Tag.WALL)  # add tag giving into init

                    net[k, f] = Tag.HAS_NODE
                    nodelist.append(x)


    for j in range(0, len(nodelist)):  # go through all nodes you found and connect them
            nodelist[j].connect(net, nodelist)
            if nodelist[j].tag == Tag.START:
                initstack.append(nodelist[j])
                print("have beginning of the list")

    path = solvethemaze(initstack)
    print(path)

if __name__ == "__main__":
    main()
