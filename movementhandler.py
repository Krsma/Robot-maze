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
        y_axis = x[0]*10 + 5
        x_axis = x[1]*10 + 5
        text = str(currentpos)
        cv2.putText(output_image,text,(x_axis,y_axis),font, font_scale,font_color,line_type)
        currentpos +=1

    cv2.imshow('image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return