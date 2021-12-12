#!/usr/bin/python3
import numpy as np

def flashFest(octoMap,haveFlashed):
    done=True
    nX,nY=octoMap.shape

    # If haveFlashed is empty, 1st call incrment energy
    if len(haveFlashed)==0:
        octoMap+=1

    # Find points that will ( or have ) flashed this step
    xFlash,yFlash = np.where(octoMap>9)
    
    for i in range(len(xFlash)):
        x=xFlash[i]
        y=yFlash[i]

        # If this has already flashed this step, continue to next point
        if (x,y) in haveFlashed:
            continue

        # New flasher, we are not done
        done=False

        # Add point into have-flashed list
        haveFlashed.append((x,y))

        # increment energy of neighbors
        for xo,yo in [ (-1,0), (1,0), (0,-1), (0,1), (-1,1), (1,-1), (-1,-1), (1,1)]:
            if x+xo>=0 and x+xo<nX and y+yo>=0 and y+yo<nY:
                octoMap[x+xo,y+yo]+=1

    # energy increments complete, recurse
    if not done:
        # Call this function again, with history
        flashFest(octoMap,haveFlashed)

    # reachable when done
    # Set all flashed points to zero energy
    for (x,y) in haveFlashed:
        octoMap[x,y]=0
    return(octoMap,len(haveFlashed))



# Read input file
#f=open('example.txt');
f=open('input.txt');
lines=f.readlines()
f.close()

# Assuming square map
octoMap=np.zeros([len(lines),len(lines)],'int32')
cnt=0
for line in lines:
    octoMap[cnt,:]=[int(x) for x in line.strip()]
    cnt+=1

# Loop initialization
cnt=0
total=0
firstSync=0
done=False

# Step through
while not done:
    cnt+=1
    octoMap,flashCount = flashFest(octoMap,[])

    # total for first 100 steps
    if cnt<100:
        total+=flashCount

    # find first sync
    if flashCount==100 and firstSync==0:
        firstSync=cnt

    # exit criteria, partA and partB solutions found
    if cnt>100 and firstSync>0:
        done=True

print("The answer to Part A is {0:d}".format(total))
print("The answer to Part B is {0:d}".format(firstSync))


