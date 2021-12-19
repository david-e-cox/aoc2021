#!/usr/bin/python3
import numpy as np

# Display folder paper
def printMap(paper):
    nX,nY=paper.shape;
    for j in range(nY):
        print("   ",end='')
        for i in range(nX):
            if paper[i,j]:
                print('#',end='')
            else:
                print('.',end='')
        print('')

# Folding with numpy fliplr and flipud
def foldHoriz(paper,atY):
    nX,nY=paper.shape
    newPaper = paper[:, :atY] + np.fliplr(paper[:,atY+1:])
    return(newPaper)

def foldVert(paper,atX):
    nX,nY=paper.shape
    newPaper = paper[:atX,:] + np.flipud(paper[atX+1:,:])
    return(newPaper)


# Read input file
#f=open('example.txt');
f=open('input.txt');

# Oversized paper
paper = np.zeros([1500,1000],'int32')

line=f.readline().strip()
while(len(line)>1):
    ij = [int(x) for x in line.split(',')]
    paper[ij[0],ij[1]]=1
    line=f.readline().strip()

# Now read folding instructions    
line=f.readline().strip()
instruct=[]
while(line):
    tmp=line.split('=')
    instruct.append( (tmp[0][-1],int(tmp[1])) )
    line=f.readline().strip()

# Cut paper down to size
# Note: not fully general, assumes x,y or y,x initial fold sequence
if instruct[0][0]=='x':
    paper=paper[:instruct[0][1]*2+1,:instruct[1][1]*2+1]
else:
    paper=paper[:instruct[1][1]*2+1,:instruct[0][1]*2+1]
    
cnt=0
for (direc,loc) in instruct:
    if direc=='y':
        paper = foldHoriz(paper,loc)
    else:
        paper = foldVert(paper,loc)
    if cnt==0:
        partA = len(np.where(paper>0)[0])
    cnt+=1


print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is:")
printMap(paper)

