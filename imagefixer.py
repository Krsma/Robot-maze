import cv2
import numpy as np

img = cv2.imread('paint.jpg')
found=False
leftmost=[0,0]
rightmost=[0,0]
downmost=[0,0]
topmost=[0,0]
for i in range(0,img.shape[0]):
  for j in range(0,img.shape[1]):
   px=img[i,j]
   if px[0]<30 and px[1]<30 and px[2]<30:
    leftmost[1]=j
    leftmost[0]=i
    found=True
  if found:
    break
found=False

for i in range(img.shape[0],0):
  for j in range(img.shape[1],0):
   px=img[i,j]
   if px[0]<30 and px[1]<30 and px[2]<30:
    rightmost[0]=i
    rightmost[1]=j
    found=True
  if found:
    break
found=False

for i in range(img.shape[1],0):
  for j in range(0,img.shape[0]):
   px=img[i,j]
   if px[0]<30 and px[1]<30 and px[2]<30:
    topmost[0]=i
    topmost[1]=j
    found=True
  if found:
    break
found=False

for i in range(0,img.shape[1]):
  for j in range(0,img.shape[0]):
   px=img[i,j]
   if px[0]<30 and px[1]<30 and px[2]<30:
    topmost[0]=i
    topmost[1]=j
    found=True
  if found:
    break
found=False


pts1 = np.float32([[leftmost[0],leftmost[1]],[topmost[0],topmost[1]],[downmost[0],downmost[1]],[rightmost[0],rightmost[1]]])
pts2 = np.float32([[0,0],[1000,0],[0,1000],[1000,1000]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(1000,1000))

cv2.imwrite('rezultatodM.jpg', dst)
