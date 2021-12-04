#!/usr/bin/python3
import numpy as np

# Read input file
#f=open('example.txt');
f=open('input.txt');

# Get dice roll
diceRoll = [int(val) for val in f.readline().split(',')];
f.readline();

# boards are 5x5 with numbers
# markers are 5x5 array with ones on entries which have been called
# allBoards, allMarkers are a list, created by appending 5x5 numpy arrays
allBoards = []
allMarks  = []

line=f.readline().strip()
while(len(line)):
    board=np.empty([5,5],'int32')
    for i in range(5):
        board[i,:]=[int(val) for val in line.split()]
        line=f.readline()
    allBoards.append(board)
    line=f.readline()
f.close()

#Initialize empty marker arrays
for i in range(len(allBoards)):
    allMarks.append(np.zeros([5,5],'int32'))

done=False
finalScore=np.zeros(len(allBoards))
for roll in diceRoll:
    # Check if last board has won, break out of loop
    if done:
        break

    # for each board, check roll see if it's won
    for i in range(len(allBoards)):
        marks = np.where(allBoards[i]==roll)
        allMarks[i][marks]=1
        # If any row or col in the marker boards adds up to 5 => BINGO
        if np.any(np.sum(allMarks[i],axis=0)==5) or np.any(np.sum(allMarks[i],axis=1)==5):
            # score is last roll times sum of entries with no marker on them
            score=roll*np.sum(allBoards[i][np.where(allMarks[i]==0)])

            # If this is the first board to score, mark winner
            if all(finalScore==0):
                winScore=score

            # If this board just won this round, mark it's score as final
            if (finalScore[i]==0):
               finalScore[i]=score

            # If this is the last board to complete, mark last score and toggle done flag
            if all(finalScore>0):
                lastScore=score
                done=True
                break

            
print("The answer to Part A is {0:d}".format(winScore))
print("The answer to Part B is {0:d}".format(lastScore))


