#!/usr/bin/python3
import numpy as np

def printMap(paper):
    nX,nY=paper.shape;
    for j in range(nY):
        for i in range(nX):
            if paper[i,j]:
                print('#',end='')
            else:
                print('.',end='')
        print('')

# Folding with numpy fliplr and flipud
# stacking zeros in here to handle folds not in the middle of the paper
def foldHoriz(paper,atY):
    nX,nY=paper.shape
    if atY >= np.floor(nY/2):
        newPaper = paper[:, :atY] + np.hstack( ( np.zeros([nX, nY-2*atY-1],'int32') ,np.fliplr(paper[:,atY+1:]) ) )
    else:
        newPaper = np.hstack( (np.zeros([nX,nY-2*atY-1],'int32'), paper[:, :atY]) ) + np.fliplr(paper[:,atY+1:])
    return(newPaper)

def foldVert(paper,atX):
    nX,nY=paper.shape
    if atX >= np.floor(nX/2):
        newPaper = paper[:atX,:] + np.vstack( ( np.zeros([nX-2*atX-1,nY],'int32') ,np.flipud(paper[atX+1:,:])))
    else:
        newPaper = np.vstack( (np.zeros([nX-2*atX-1,nY],'int32'), paper[:atX,:]) ) + np.flipud(paper[atX+1:,:])
    return(newPaper)

# Read input file
#f=open('example.txt');
f=open('input.txt');

# These dimensons are critical
# I stumbled onto them....  not sure how we are supposed to determine the initial paper size
paper = np.zeros([1311,895],'int32')

line=f.readline().strip()
while(len(line)>1):
    ij = [int(x) for x in line.split(',')]
    paper[ij[0],ij[1]]=1
    line=f.readline().strip()

line=f.readline().strip()
instruct=[]
while(line):
    tmp=line.split('=')
    instruct.append( (tmp[0][-1],int(tmp[1])) )
    line=f.readline().strip()

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

