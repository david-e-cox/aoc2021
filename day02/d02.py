#!/usr/bin/python3
import numpy as np

# Read input file


f=open('input.txt','r');
lines = f.readlines();

Hpos=Dpos=0
for line in lines:
    [direction,distance]=line.split();
    if direction == 'forward':
        Hpos+=int(distance)
    elif direction == 'up':
        Dpos-=int(distance)
    elif direction =='down':
        Dpos+=int(distance)
    else:
       print("error")
       exit()
        
print("The answer to Part A is {0:d}".format(Hpos*Dpos))



Hpos=Dpos=aim=0
for line in lines:
    [direction,distance]=line.split();
    if direction == 'forward':
        Hpos+=int(distance)
        Dpos+=aim*int(distance)
    elif direction == 'up':
        aim-=int(distance)
    elif direction =='down':
        aim+=int(distance)
    else:
       print("error")
       exit()

print("The answer to Part B is {0:d}".format(Hpos*Dpos))

