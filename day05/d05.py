#!/usr/bin/python3
import numpy as np

# Display map to screen 
def printMap(map):
    for j in range(map.shape[0]):
        for i in range(map.shape[1]):
            if map[i,j]==0:
                print('.',end='')
            else:
                print("{0:d}".format(map[i,j]),end='')
        print('')

# Read input file
#f=open('example.txt')
f=open('input.txt')
lines=f.readlines()
f.close;

# Allocate storage for end point coordiantes
nPts = len(lines)
x0 = np.empty(nPts,'int32')
y0 = np.empty(nPts,'int32')
x1 = np.empty(nPts,'int32')
y1 = np.empty(nPts,'int32')

# Read in data
for i in range(nPts):
    tmp = lines[i].split();
    x0[i],y0[i] = [int(s) for s in tmp[0].split(',')]
    x1[i],y1[i] = [int(s) for s in tmp[2].split(',')]

# Alloate Map
sizeX=np.max([np.max(x0),np.max(x1)])+1
sizeY=np.max([np.max(y0),np.max(y1)])+1
mapA = np.zeros([sizeX,sizeY],'int32')
mapB = np.zeros([sizeX,sizeY],'int32')

# Increment map for lines between end points
for i in range(nPts):
    xmin=np.min([x0[i],x1[i]])
    xmax=np.max([x0[i],x1[i]])
    ymin=np.min([y0[i],y1[i]])
    ymax=np.max([y0[i],y1[i]])
    if xmin==xmax : # Vertical
        mapA[xmin,list(range(ymin,ymax+1))] += 1
    elif ymin==ymax: # Horizontal
        mapA[list(range(xmin,xmax+1)),ymin] += 1
    else:
        # default: slopes positive, both dimensions
        xStart=x0[i];  xEnd=x1[i]+1;
        yStart=y0[i];  yEnd=y1[i]+1
        xStep=1;       yStep=1
        # fix for negative slopes
        if x0[i]>x1[i]:
            xStart=x0[i];  xEnd=x1[i]-1; xStep=-1
        if y0[i]>y1[i]:
            yStart=y0[i];  yEnd=y1[i]-1; yStep=-1
        # Increment map along diagonals
        xcoors = list(range(xStart,xEnd,xStep))
        ycoors = list(range(yStart,yEnd,yStep))
        mapB[xcoors,ycoors] += 1

#Display for example
if sizeX<100:
    printMap(mapA+mapB)

#Compute solutions
partA = len(np.where(mapA>=2)[0])
partB = len(np.where(mapA+mapB>=2)[0])
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


