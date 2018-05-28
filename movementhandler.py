import cv2
import numpy


def writepath(path,image):
    currentpos = 1

    output_image = image    # variable selection
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.1
    font_color = (0,255,0)
    line_type = 2

    for x in path:      # numbering the path
        #  y_axis = x[0]*10 + 5
        #  x_axis = x[1]*10 + 5
        #  text = str(currentpos)
        #  cv2.putText(output_image,text,(x_axis,y_axis),font, font_scale,font_color,line_type)   # TO DO: Arrows instead of text
        writearrow(x, path, output_image)
        currentpos +=1

    # TO DO: image scaling before outputing on the screencv2.reSize to full resolution
    output_image = cv2.resize(output_image, None, fx = 4, fy = 4, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return


# if you can avoid the code bellow this point please do
# The code written there is an abomination, not even the Devil himself wouldn't force somebody to read it
# It is a steaming pile of shit, which works god knows why. Its filled with mixed up variables name and plenty other war crimes
# Please seek help if somebody forces you to read that code
# https://www.iasp.info/
# If the code stops working for some reason, sacrifice a goat to the Cthulhu and ask for help


def finddirection(field1,field2):
    if (field1[0] > field2[0]):
        return "left"
    elif (field1[0] < field2[0]):
        return "rigth"

    if (field1[1] > field2[1]):
        return "up"
    elif (field1[1] < field2[1]):
        return "down"
    else:
        return

def setup_field1(field,direction):

    if (direction == "up"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5

    elif (direction == "down"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5

    elif (direction == "left"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5

    elif (direction == "rigth"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5
    else:
        return
    position = (y,x)
    return position

def setup_field2(field, direction):

    if (direction == "up"):
        x = field[0]*10 + 5
        y = field[1]*10

    elif (direction == "down"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5

    elif (direction == "left"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5

    elif (direction == "rigth"):
        x = field[0]*10 + 5
        y = field[1]*10 + 5
    else:
        return
    position = (y,x)
    return position

def writearrow(field,path,image):
    x = field

    if (path.index(field) + 1 == len(path)):
        return
    else:
        y = path[path.index(field) + 1]

    COLOR = (255,0,0)
    THICK = 1
    LINE_TYPE = 8
    SHIFT = 0
    TIP_LENGTH = 0.25

    cv2.arrowedLine(image, setup_field1(x, finddirection(x, y)), setup_field2(y, finddirection(x, y)), COLOR, THICK, LINE_TYPE, SHIFT, TIP_LENGTH)
