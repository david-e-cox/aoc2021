#!/usr/bin/python3
import numpy as np
from collections import defaultdict

# A-Star algorithm, straight from Wikipedia
def reconstruct_path(cameFrom, current):
    totalPath = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        totalPath.append(current)
    totalPath.reverse()
    return totalPath

def h(goal,pt):
    # Manhattan distance
    return( abs(goal[0]-pt[0]) + abs(goal[1]-pt[1]))

def astar(start,goal,riskMap):
    offsets = [(1,0), (-1,0), (0,1), (0,-1)]
    openSet = {start}
    cameFrom = {}
    gScore = defaultdict(lambda:1e9)
    gScore[start] = 0

    fScore =defaultdict(lambda:1e9)
    fScore[start] = h(goal,start)


    while len(openSet):
        minValue=1e9
        for loc in openSet:
            if fScore[loc]< minValue:
                current = loc
                minValue=fScore[loc]

        if current == goal:
            return reconstruct_path(cameFrom,current)

        openSet.remove(current)
        for move in offsets:
            pos = np.array(move)+np.array(current)
            if pos[0]>=0 and pos[0]<riskMap.shape[0] and pos[1]>=0 and pos[1]<riskMap.shape[1]:
                neighbor=(pos[0],pos[1])
                tentative_gScore = gScore[current] + riskMap[neighbor]
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + h(goal,neighbor)
                    
                    if neighbor not in openSet:
                        openSet.add(neighbor)
    
    
# Read input file
#f=open('example.txt');
f=open('input.txt');

line=f.readline().strip()
nCols = len(line)
riskMapA  = np.zeros([0,nCols],'int32')
while(line):
    tmp = [int (x) for x in line]
    riskMapA = np.append(riskMapA,[tmp],axis=0)
    line = f.readline().strip()
f.close()


# Goal is bottom right corner
endPt = (riskMapA.shape[0]-1,riskMapA.shape[1]-1)
# Call astar for optimal path
path = astar((0,0),endPt,riskMapA)
# Calculate risk along path, 1st point doesn't count in total
totalRiskA=-riskMapA[path[0]]
for loc in path:
    totalRiskA += riskMapA[loc]


# Part B
riskRow= riskMapA
# Expand map

# Silly %10+1 stuff here to generate map
nextSection = riskMapA
# Expand to the right
for i in range(4):
    nextSection = (nextSection+1)%10
    nextSection = np.where(nextSection==0,1,nextSection)
    riskRow = np.append(riskRow, nextSection ,axis=1)
# Expand down
riskMapB=riskRow
nextSection=riskRow
for i in range(4):
    nextSection = (nextSection+1)%10
    nextSection = np.where(nextSection==0,1,nextSection)
    riskMapB = np.append(riskMapB, nextSection ,axis=0)

# Set new goal    
endPt = (riskMapB.shape[0]-1,riskMapB.shape[1]-1)
# Solve for path
path = astar((0,0),endPt,riskMapB)
# Calculate total risk along path, neglecting first point
totalRiskB=-riskMapB[(0,0)]
for loc in path:
    totalRiskB += riskMapB[loc]

print("The answer to Part A is {0:d}".format(totalRiskA))
print("The answer to Part B is {0:d}".format(totalRiskB))


