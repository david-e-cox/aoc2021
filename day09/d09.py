#!/usr/bin/python3
import numpy as np

def growbasin(surf,basin,pts):
    # Given a set points and basin, extend outward with new points
    newPts = set()
    nX,nY=surf.shape;
    
    while(pts):
        x,y=pts.pop()
        lowPt = surf[x,y]
        DnUpLfRt=[ (x+1,y),(x-1,y),(x, y-1),(x, y+1) ]
        
        for pt in DnUpLfRt:
            # If not exceeding boundaries
            if pt[0]<nX and pt[0]>=0 and pt[1]<nY and pt[1]>=0:
                # if point is larger than starting point, but not a 9
                if surf[pt]>lowPt and surf[pt]<9:
                    # Add that as a new point in the basin
                    newPts.add(pt)
    # Remove points which are ready in the basin, not really new
    newPts=newPts-basin
    # Add new points to basin
    newBasin = basin|newPts
    # return
    return(newBasin,newPts)
    
# Read input file
#f=open('example.txt');
f=open('input.txt');

surfData=np.array([],'int32')
line=f.readline().strip()
nX=len(line)
nY=0
while(len(line)):
    surfData=np.append(surfData,np.array([int(x) for x in line]))
    nY+=1
    line=f.readline().strip()

surf=np.reshape(surfData,[nY,nX])
surfMap=np.zeros([surf.shape[0]+2,surf.shape[1]+2],'int32')
surfMap[1:-1,1:-1]=surf
surfMap[1:-1, 0]  = 10*np.ones(nY)
surfMap[0, 1:-1]  = 10*np.ones(nX)
surfMap[1:-1, -1] = 10*np.ones(nY)
surfMap[-1, 1:-1] = 10*np.ones(nX)

diffX1 = surfMap[1:-1,1:-1] - surfMap[2:  ,1:-1]
diffX2 = surfMap[1:-1,1:-1] - surfMap[0:-2,1:-1]
diffY1 = surfMap[1:-1,1:-1] - surfMap[1:-1,2:]
diffY2 = surfMap[1:-1,1:-1] - surfMap[1:-1,0:-2]

ndxLow = np.where( (diffX1<0) & (diffX2<0) & (diffY1<0) & (diffY2<0) )


############## Part B ################

# Size of each basin
bSize=[]

# For all the low points found in part-A
for i in range(len(ndxLow[0])):
    basin = set()
    pts   = set()
    pts.add(  (ndxLow[0][i],ndxLow[1][i]) )
    basin.add((ndxLow[0][i],ndxLow[1][i]) )
    # Starting at a low point, expand basin outward
    # until now new points can be added
    while (pts):
        basin,pts = growbasin(surf,basin,pts)
    # Add size of this basin to list
    bSize.append(len(basin))

#Sort basin size list, compute product of three largest for solution
bSize.sort()
partB = bSize[-3]*bSize[-2]*bSize[-1]

print("The answer to Part A is {0:d}".format(np.sum(surf[ndxLow]+1)))
print("The answer to Part B is {0:d}".format(partB))


