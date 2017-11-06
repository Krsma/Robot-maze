from netmaker import buildnet, readImage

class node(object):
    north = None
    south = None
    west = None
    east = None
    tag = 0  # tag 5 is the final of the maze, tag 2 for the start, tag 1 for regular nodes
    positionx = 0
    positiony = 0
    beenhere = False

    def __init__(self, positionx, positiony, tag):
        self.positiony = positiony
        self.positionx = positionx
        self.tag = tag

    def connect(self, net, nodelist):  # making connections to other nodes, there probably is a better way to do this
        for i in range(self.positiony, 15):
            if net[self.positionx, i] == 4:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positiony == i) and (nodelist[j].positionx == self.positionx):
                        self.east = nodelist[j]
                        break

            elif net[self.positionx, i] == 1:
                break


        for i in range(1, self.positiony):  # edge is always 1 so we skip that one
            if net[self.positionx, i] == 4:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positiony == i) and (nodelist[j].positionx == self.positionx):
                        self.west = nodelist[j]
                        break

            elif net[self.positionx, i] == 1:
                break


        for j in range(self.positionx, 15):
            if net[j, self.positiony] == 4:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positionx == i) and (nodelist[j].positiony == self.positiony):
                        self.south = nodelist[j]
                        break

            elif net[j, self.positiony] == 1:
                break

        for j in range(1, self.positionx):  # evading the edge
            if net[j, self.positiony] == 4:
                for j in range(0, len(nodelist)):
                    if (nodelist[j].positionx == i) and (nodelist[j].positiony == self.positiony):
                        self.north = nodelist[j]
                        break

            elif net[j, self.positiony] == 1:
                break

def solvethemaze(nodm):
    if len(nodm) == 0:
        print("List is empty")
        return
    current = nodm[len(nodm) - 1]  # take last node


    if not(current.east.tag==None):
          if (current.east.tag == 5):
             nodm.append(current.east)
             return(nodm)

          elif (not(current.east.tag == 5) and (current.east.beenhere == False)):
             current.beenhere = True
             nodm.append(current.east)
             solvethemaze(nodm)

    if not(current.west.tag==None):
          if (current.west.tag == 5):
              nodm.append(current.west)
              return(nodm)

          elif(not(current.west.tag == 5) and (current.west.beenhere == False)):
             current.beenhere = True
             nodm.append(current.west)
             solvethemaze(nodm)

    if not(current.north.tag==None):
         if (current.north.tag == 5):
             nodm.append(current.north)
             return(nodm)

         elif(not(current.north.tag == 5) and (current.north.beenhere == False)):
            current.beenhere = True
            nodm.append(current.north)
            solvethemaze(nodm)
    if not(current.south.tag==None):
        if (current.south.tag == 5):
            nodm.append(current.south)
            return(nodm)

        elif(not(current.south.tag == 5) and (current.south.beenhere == False)):
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
            if not(net[k, f] == 1):
                a = (net[k, f + 1] == 1)
                b = (net[k, f - 1] == 1)
                c = (net[k + 1, f] == 1)
                d = (net[k - 1, f] == 1)
                if (((a and not b) or (b and not a)) or ((c and not d) or (d and not c))) or (net[k, f] == 5) or (net[k, f] == 2):
                    # i slightly changed this algorithm
                    # https://youtu.be/rop0W4QDOUI?t=7m56s
                    if net[k, f] == 5:
                        x = node(k, f, 5)
                    elif net[k, f] == 2:
                        x = node(k, f, 2)
                    else:
                        x = node(k, f, 1)  # add tag giving into init

                    # print(k)
                    # print(f)
                    # print()
                    net[k, f] = 4  # tag 4 represents that this field contains the node
                    nodelist.append(x)


    for j in range(0, len(nodelist)):  # go through all nodes you found and connect them
            nodelist[j].connect(net, nodelist)
            if nodelist[j].tag == 2:
                initstack.append(nodelist[j])
                print("have beginning of the list")

    path = solvethemaze(initstack)
    print(path)

if __name__ == "__main__":
    main()
