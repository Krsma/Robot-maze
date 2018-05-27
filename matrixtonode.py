from netmaker import buildnet, findstart, readImage, Tag
from valuechecker import check_buildnet,check_img
from movementhandler import writepath
imgname = "lavirinttesst.jpg"
path = []

def solvemaze(x,y,net):
    global path
    if net[x,y] == Tag.FINAL:
        position = (x, y)
        path.append(position)  # saving the coordinates in a tuple
        print("found end")
        return True
    elif net[x,y] == Tag.WALL:
        return False
    elif net[x,y] == Tag.VISITED :
        return False

    net[x,y] = Tag.VISITED

    if (solvemaze(x+1,y,net) or solvemaze(x-1,y,net) or solvemaze(x,y+1,net) or solvemaze(x,y-1,net)):
        position = (x,y)  # tuple containing the position of the field
        path.append(position)
        return True

    return False


def main():
    img = readImage(imgname)
    if check_img(img) == False:
        return

    global path
    path = []

    net = buildnet(img)

    start = findstart()
    solvemaze(start[0], start[1], net)
    path.reverse()  # reversing the string so that it starts from the start towards the end
    for x in path:
        print(x[0], x[1])

    writepath(path,img)


if __name__ == "__main__":
    main()
