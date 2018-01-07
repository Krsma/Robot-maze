from netmaker import buildnet, readImage, Tag
import numpy as np

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

def find_node(nodelist, x, y):
    for n in nodelist:
        if n.positionx == x and n.positiony == y:
            return n


def checklist(a):  # function for checking if received list isnt empty
    if a is None:
        return "not a list"
    if not a: # pythonic way of checking if list is empty using implied boolean value of an empty list
        return "list is empty"
    return True

def check_path(a): # checking if found path is valid
    if not a:
        return "list is empty"
    found_start = False
    found_end = False
    for i in a:
        if a.tag == Tag.START:
            found_start = True
        if a.tag == Tag.FINAL:
            found_end = True

    if found_start == False:
        if found_end == False:
            return "no end and no start"
        else:
            return "no start found"
    if found_end == False:
        return "no end found"

    return  True


def check_connect_all(a):   #function for checking if all nodes in given list have at least 1 connection
    for i in a:
        if not ((i.north != None) or (i.south != None) or (i.west != None) or (i.east != None)):
            return "there are nodes with no connections"
    return True

def check_img(img):
    if img is None: # check if img read failed
        return "image failed to load"
    return True

def check_buildnet(net):
    if not net.size == 225: #net.size should return 225 (15*15) if every element of the net contains a value
        return "net isn't completly filled"
    for i in range(0, net.shape[0]): #checking if any element of net is invalid (in sense that it isnt one of the defined values)
        for j in range(0, net.shape[1]):
            if not ((net[i, j] == Tag.START) or (net[i, j] == Tag.PATH) or (net[i, j] == Tag.WALL) or (net[i, j] == Tag.FINAL)):
                return "invalid data in the net"
    return True







def main():
    print("value checking module")


if __name__ == "__main__":
    main()