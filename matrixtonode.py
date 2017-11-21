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


def solvethemaze(path):
    if len(path) == 0:
        print("List is empty")
        return
    current = path[- 1]  # take last node

    if current.tag == 5:
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


def main():
    img = readImage("lavirinttesst.jpg")
    if (img is None):
        return

    nodelist = []
    path = []

    net = buildnet(img)

    for k in range(0, 14):  # should be changed to 0..14 and the 15 line is used as an edge
        for f in range(0, 14):
            if not (net[k, f] == Tag.WALL):
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
            path.append(nodelist[j])
            # print("have beginning of the list")

    path = solvethemaze(path)
    print(path)


if __name__ == "__main__":
    main()
