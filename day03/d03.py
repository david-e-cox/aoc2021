#!/usr/bin/python3
import numpy as np

# bitFilter routine 
def bitFilter(data,doLeastCommon):
    if doLeastCommon:
        invert=1;
    else:
        invert=0;
        
    nCols=data.shape[1]
    value=-1
    for i in range(nCols):
        nOnes  = np.int32(np.sum(data[:,i]))
        nZeros = data.shape[0]-nOnes
        # Nominally do most common as target value with invert=0
        # if doLeastCommon is true invert=1 with swap targetValue
        if (nOnes>=nZeros):
            targetValue=1-invert
        else:
            targetValue=invert
        # Rows where active bit has targetValue
        ndx = np.squeeze(np.argwhere(data[:,i]==targetValue))
        # Slice for new data
        data=data[ndx,:]
        # If data is a single row, stop
        if len(data.shape)==1:
            # map vector into string, then cast string as base-2 number into decimal
            value = int(''.join(list(map(lambda x:str(x), data))),2)
            break
    return(value)


# Read input file
#f=open('example.txt');
f=open('input.txt');

lines=f.readlines();
f.close()

# Parse file into numpy array of 0/1 values
nRows = len(lines)
nCols = len(lines[0].strip())
data=np.empty([nRows,nCols],'int32')
print(data.shape)
for i in range(0,nRows):
    for j in range(0,nCols):
        string=lines[i].strip()
        data[i,j]=int(string[j])

# sum along columns, normalize and round to determine majority
gammaVec = np.int32(np.round(np.sum(data,axis=0)/nRows))
gammaStr = ''.join(list(map(lambda x: str(x),gammaVec)))
gammaRate = int(gammaStr,2)

# invert gammaVec for epsilon
epsilonVec = 1-gammaVec
epsilonStr = ''.join(list(map(lambda x: str(x),epsilonVec)))
epsilonRate = int(epsilonStr,2)

print("The answer to Part A is {0:d}".format(gammaRate*epsilonRate))
print("The answer to Part B is {0:d}".format(bitFilter(data,False)*bitFilter(data,True)))


