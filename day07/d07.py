#!/usr/bin/python3
import numpy as np

# Read input file
f=open('input.txt');

pos = np.array([int(x) for x in f.readline().split(',')])
nSpiders = len(pos)
nRange   = np.max(pos)

total=np.zeros(nRange,'int32')
for i in range(nRange):
    total[i] = np.sum(abs(pos-i))
costA = np.min(total)
optPosA = np.argmin(total)


total=np.zeros(nRange,'int32')
for i in range(nRange):
    total[i] += np.sum( (np.power(pos-i,2)+abs(pos-i)) / 2)
    # The slow way...
    #for j in range(nSpiders):
        #if pos[j]!=i:
            #distVec = list(range(1,abs(pos[j]-i)+1))
            #total[i] += np.matmul(distVec,np.ones([len(distVec),1]))
costB = np.min(total)
optPosB = np.argmin(total)

print("The answer to Part A is {0:d}".format(costA))
print("The answer to Part B is {0:d}".format(costB))


