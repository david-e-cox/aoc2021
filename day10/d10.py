#!/usr/bin/python3
from collections import defaultdict

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.readlines()
f.close()

# Mappings
pointsA    = { ')':3, ']':57, '}':1197, '>':25137 }
pointsB    = { ')':1, ']':2,  '}':3,    '>':4 }
openChar  = ['(','[','{','<'];
closeChar = [')',']','}','>'];
typeMap   = {'(':0, ')':0,
             '[':1, ']':1,
             '{':2, '}':2,
             '<':3, '>':3 }

# Score and Score List for Parts A/B
totalA=0;
totalB=[];

for l in lines:
    # Assume the best
    badLine=False
    lastOpen=[];
    line = l.strip()
    
    for c in line:
        if c in openChar:
            # Track the opening character sequence
            lastOpen.append(typeMap[c])
        elif c in closeChar:
            # Check the last open (pop() will remove it)
            openType=lastOpen.pop()
            if openType != typeMap[c]:
                #print("- {}  Expected {} but found {} instead.".format(line,closeChar[openType],c))
                totalA += pointsA[c]
                badLine=True
        else:
            # Shouldn't happen
            print("Unknown character found {}".format(c))
    # For part B, on good lines find closing character stream.
    # It's already stored in lastOpen array
    if not badLine:
        cList=[]
        while(lastOpen):
            cList.append(closeChar[lastOpen.pop()])
        score=0
        for c in cList:
            score = 5*score + pointsB[c]
        totalB.append(score)
        #print("{} Complete by adding {} for points {}".format(line,''.join(cList),score))

totalB.sort()
print("The answer to Part A is {0:d}".format(totalA))
print("The answer to Part B is {0:d}".format(totalB[int(len(totalB)/2)]))


