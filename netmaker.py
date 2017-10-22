import cv2
import numpy as np

def readImage(imageFileName):
    img = cv2.imread(imageFileName)
    if(img is None):
        print("File " + imageFileName + " not found.")
    return img 

def buildnet(img):
    # tag 2 is for start
    # tag 5 is for end of the maze
    # tag 1 is for wall
    # tag 0 is for path
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowGreen = np.array([40, 100, 100])
    upGreen = np.array([80, 255, 255])
    greenMask = cv2.inRange(hsv, lowGreen, upGreen)

    lowRed = np.array([0, 50, 50])
    upRed = np.array([50, 255, 255])
    redMask = cv2.inRange(hsv, lowRed, upRed)

    cv2.imshow('img', img)
    cv2.imshow('greenMask', greenMask)
    cv2.imshow('redMask', redMask)

    net = np.zeros(shape=(15, 15))
    # TODO: add logic here
    for a in range(0, 15):
        for b in range(0, 15):
            net[a, b] = 2

    return net

def printNet(net):
    for i in range(0, 15):
        for j in range(0, 15):
            print (net[i, j] + " ")
        print("\n")

def main():
    img = readImage("lavirinttesst.jpg")
    if(img is None):
        return
    
    net = buildnet(img)
    print(net)
    
    cv2.waitKey(0)

if __name__ == "__main__":
    main()

