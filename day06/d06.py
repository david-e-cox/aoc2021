#!/usr/bin/python3
import numpy as np
from collections import defaultdict

# Read input file
#f=open('example.txt');
f=open('input.txt');
rawString = f.readline()
f.close()

fish0 = np.array([int(x) for x in rawString.split(',')])

# Part-A: generating all members.  Count for total
fish=np.copy(fish0)
for day in range(80):
    fish -= 1
    ndx=np.asarray(fish<0).nonzero()
    fish[ndx[0]]=6;
    fish=np.append(fish,8*np.ones(len(ndx[0]),'int32'))


    
# Part-B
# Simulation population, track only total at each age

# Initialize state vector for fish population at different ages
fishState=np.zeros(9,'int64');    
for age in range(9):
    fishState[age] += len(np.asarray(fish0==age).nonzero()[0])

# Create state transition matrix x(k+1) = Ax(k)
# Shifts count-down age, respawns and adds offspring
A = np.diagflat(np.ones(8,'int64'),1)
A[6,0]=1; # Respawn
A[8,0]=1  # Children

# Simulation population
for day in range(256):
    fishState = np.matmul(A,fishState)

print("The answer to Part A is {0:d}".format(len(fish)))
print("The answer to Part B is {0:d}".format(np.sum(fishState)))



