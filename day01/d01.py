#!/usr/bin/python3
import numpy as np

# Read input file
f=open('input.txt');
inval =[int(val) for val in f.read().split()];
f.close()

increaseCnt = np.size(np.where(np.diff(inval)>0))
print("The answer to Part A is {0:d}".format(increaseCnt))

mavg=np.convolve(inval,[1,1,1],mode='valid')
increaseCnt = np.size(np.where(np.diff(mavg)>0))
print("The answer to Part B is {0:d}".format(increaseCnt))


