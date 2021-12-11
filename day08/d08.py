#!/usr/bin/python3
import numpy as np
from collections import defaultdict

# Read input file
#f=open('example.txt');
f=open('input.txt');

inp=[]
out=[];
line=f.readline()
while len(line):
    inStr,outStr = line.strip().split('|')
    inp.append(inStr.split())
    out.append(outStr.split())
    line=f.readline()
f.close()    

#Initialize variables
count=0
uniqueDig=[]
total=0;
fullSet={'a','b','c','d','e','f','g'}

#Nominal mapping from 7-segment signal set to number
#keys are sorted signal sets
numberDict = defaultdict(lambda:-10000)
numberDict['abcefg'] = 0;
numberDict['cf']     = 1;
numberDict['acdeg']  = 2;
numberDict['acdfg']  = 3;
numberDict['bcdf']   = 4;
numberDict['abdfg']  = 5;
numberDict['abdefg'] = 6;
numberDict['acf']    = 7;
numberDict['abcdefg']= 8;
numberDict['abcdfg'] = 9;

# Part-A: count up the unique terms
for i in range(len(out)):
    for dig in out[i]:
        if len(dig)==2 or len(dig)==3 or len(dig)==4 or len(dig)==7:
            count+=1
            uniqueDig.append(dig)


#Part-B: work through all input/output lines
for i in range(len(inp)):
    # Create sets of on-segments and off-segements, organized by number of segments active
    onSet =defaultdict(lambda: set())
    offSet=defaultdict(lambda: set())
    mapping=defaultdict(lambda: '')
    used=set()
    for dig in inp[i]:
        for c in dig:
            onSet[len(dig)].add(c)
            missing = list(fullSet-set(dig))
            for uc in missing:
                offSet[len(dig)].add(uc)


    # Just if/then logic, from staring at the 7-segment patterns.
    # I can't see a better way:

    # If segment is in 3set, but not in 4set or 2set - then it is 'a'        
    c=((onSet[3]-onSet[4]) & (onSet[3]-onSet[2])).pop()
    mapping[c]='a'
    used.add(c)
 
    # If segment is in 4set, but not in 2set AND is off in 6set, then it is 'd'
    c= ((onSet[4]-onSet[2]) & offSet[6]).pop()
    mapping[c]='d'
    used.add(c)
    
    # If segment is in 4set, but not in 2set AND not yet used, then it is 'b'
    c = ((onSet[4]-onSet[2]) - used).pop()
    mapping[c]='b'
    used.add(c)
    
    # If segment is in 4set but not used AND is off in 6 set, then it is 'c'
    c = ((onSet[4] - used) & offSet[6]).pop()
    mapping[c]='c'
    used.add(c)
    
    # If segment is in 4set but not used it is 'f'
    c = (onSet[4] - used).pop()
    mapping[c]='f'
    used.add(c)
    
    # If segment is in 6set and not off in 5Set and not used, it is 'g'
    c= (onSet[6] - offSet[5] -used).pop()
    mapping[c]='g'
    used.add(c)

    # Last one
    c=(fullSet-used).pop()
    mapping[c]= 'e'
    used.add(c)

    # Mapping is done, use it to map output values to nominal display wiring
    val=0
    cnt=3
    for dig in out[i]:
        keyList=[]
        for c in dig:
            keyList.append(mapping[c])
        keyList.sort();
        keyStr=''.join(keyList)
        val+=numberDict[keyStr]*np.power(10,cnt)
        cnt-=1
    #print("{} {}".format(i,val))

    # Total value, adding in this line's readout
    total+=val

print("The answer to Part A is {0:d}".format(count))
print("The answer to Part A is {0:d}".format(total))



