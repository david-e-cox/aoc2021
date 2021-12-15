#!/usr/bin/python3
from collections import defaultdict

def applySubs(chain,rules):
    cnt=0
    done=False
    while not done:
        k = ''.join(chain[cnt:cnt+2])
        if k in rules.keys():
            chain.insert(cnt+1,rules[k])
            cnt+=2
        else:
            cnt+=1
        if (cnt-1) > len(chain):
            done=True
    return(chain)
        

# Read input file
#f=open('example.txt');
f=open('input.txt');

rules=defaultdict(lambda:'')
line = f.readline().strip()
chain=[x for x in line]
chain0=chain.copy()
line=f.readline().strip()
line=f.readline().strip()
while(line):
    pair,element=line.split(' -> ')
    rules[pair]=element
    line=f.readline().strip()


    
# Part A - direct solution    
count = defaultdict(lambda:0)
for i in range(10):
    chain=applySubs(chain,rules)
    
for j in range(len(chain)):
    count[chain[j]]+=1

val = count.values()
partA = max(val) - min(val)




#Part B, same problem but much too big for a direct construction
# looked for patterns, repeating sequences, etc...
# finally looked at reddit ;)

chain=chain0.copy()

#Dictionaries to keep track of all pairs, and all elements
pairCount=defaultdict(lambda:0)
eleCount=defaultdict(lambda:0)

#Initialize
for i in range(len(chain)-1):
    pairCount[''.join(chain[i:i+2])] += 1

for i in range(len(chain)):
    eleCount[chain[i]]+=1

#Step through time, 40 steps
# For each existing pair apply rule and increment element count by the number of existing pairs
# Also create two new pairs and add (or increment) them by the same existing-pair count
for time in range(40):
    pairs = list(pairCount.keys())
    count = list(pairCount.values())
    for i in range(len(pairs)):
        newElement = rules[pairs[i]]
        oldLeft = pairs[i][0];
        oldRight= pairs[i][1];

        # Add element created by rule into count
        eleCount[newElement] += count[i]
        # Create new pairs left/right, increment counts
        newPairLf = oldLeft    + newElement
        newPairRt = newElement + oldRight
        # Destroy the original pair
        pairCount[pairs[i]] -= count[i]
        # Add two new pairs in (left and right)
        pairCount[newPairLf]+=count[i]
        pairCount[newPairRt]+=count[i]

val = eleCount.values()
partB = max(val) - min(val)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


