import cv2
import numpy as np
from enum import Enum
import os
from time import sleep
import picamera

startpos = []
class Tag(Enum):
    PATH = 0
    WALL = 1
    START = 2
    FINAL = 5
    VISITED = 3

def getImage(imageFileName):
    if (os.name()[0] == 'raspberrypi'): #check if code is being run on a Raspberry pi, so that we can use the camera
        camera = PiCamera()
        camera.resolution = (150, 150)
        camera.start_preview()
        sleep(2)
        camera.capture('cameraoutput.jpg')
        return readImage('cameraoutput.jpg')
    else:
        return readImage(imageFileName)


def readImage(imageFileName):
    img = cv2.imread(imageFileName)
    if img is None:
        print("File " + imageFileName + " not found.")
    return img 

def buildnet(img, width = 15, height = 15, show = False):
    # tag 2 is for start
    # tag 3 is later used for visited cells
    # tag 5 is for end of the maze
    # tag 1 is for wall
    # tag 0 is for path
    img15 = cv2.resize(img, (width, height), interpolation = cv2.INTER_LINEAR)  #
    hsv = cv2.cvtColor(img15, cv2.COLOR_BGR2HSV)

    lowGreen = np.array([40, 100, 100])
    upGreen = np.array([80, 255, 255])
    greenMask = cv2.inRange(hsv, lowGreen, upGreen)
    
    lowRed = np.array([0, 50, 50])
    upRed = np.array([50, 255, 255])
    redMask = cv2.inRange(hsv, lowRed, upRed)

    if show:
        cv2.imshow('img', img)
        cv2.imshow('img15', img15)
        cv2.imshow('greenMask', greenMask)
        cv2.imshow('redMask', redMask)

    # Build net
    net = np.zeros(shape=(width, height), dtype=Tag)
    for a in range(0, width):
        for b in range(0, height):
            if greenMask[a, b] > 0:
                net[a, b] = Tag.START # tag 2 is for start
                startpos.append(a)
                startpos.append(b)
            elif redMask[a, b] > 0:
                net[a, b] = Tag.FINAL  # tag 5 is for end of the maze
            elif img15[a, b][0] > 20:
                net[a, b] = Tag.PATH  # tag 0 is for path
            else:
                net[a, b] = Tag.WALL  # tag 1 is for wall

    return net
def findstart():
    start = tuple(startpos)  # conversion of list into a tuple
    print("found start")
    return start

def printNet(net):
    for i in range(0, net.shape[0]):
        for j in range(0, net.shape[1]):
            print (net[i, j] + " ")
        print("\n")

def main():
    img = readImage("lavirinttesst.jpg")
    if(img is None):
        return
    
    net = buildnet(img, show = True)
    print(net)
    
    cv2.waitKey(0)

if __name__ == "__main__":
    main()

