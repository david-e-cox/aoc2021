#!/usr/bin/python3
from collections import defaultdict

def findAllPaths(graph,start,end,partB=False,path=[]):
    path = path + [start]

    if start==end:
        return [path]

    paths=[]
    for cave in graph[start]:
        # isolate small caves from path
        smallCaves = [c for c in path if c.islower()]
        # if the set of small caves is less than the list, at there is a duplicate already, set flag
        if len(set(smallCaves)) != len(smallCaves):
            doneDouble=True
        else:
            doneDouble=False
        # Conditions on which we continue enumerating next steps
        if (cave not in path) or (cave.isupper()) or (partB and cave.islower() and cave!='start' and not doneDouble):
            newPath = findAllPaths(graph,cave,end,partB,path)
            for new in newPath:
                paths.append(new)

    return paths


# Read input file
#f=open('example2.txt');
f=open('input.txt');

graph = defaultdict(lambda: [] )
line=f.readline().strip()
while (line):
    src,dst = line.split('-')
    # bi-directional, set src->dst and dst->source
    graph[src].append(dst)
    graph[dst].append(src)
    line=f.readline().strip()
f.close()


allA = findAllPaths(graph,'start','end',partB=False)
allB = findAllPaths(graph,'start','end',partB=True)

# Debuging on examples
if len(allA)<50:
    for p in allA:
        print("{}".format(','.join(p)))
    print()
    for p in allB:
        print("{}".format(','.join(p)))
      
print("The answer to Part A is {0:d}".format(len(allA)))
print("The answer to Part B is {0:d}".format(len(allB)))


