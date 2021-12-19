#!/usr/bin/python3
import numpy as np



def step(pos,vel):
    pos[0] += vel[0]
    pos[1] += vel[1]
    vel[0] -= np.sign(vel[0])
    vel[1] -= 1
    return pos,vel

def inTarget(pos,vel):
    #Input.txt: target area: x=201..230, y=-99..-65
    targetX=(201,230)
    targetY=(-99,-65)
    # Example.txt
#    targetX=(20,30)
#    targetY=(-10,-5)
    isLong =False
    isShort=False
    isHit  =False

    if pos[0]<=targetX[1] and pos[0]>=targetX[0] and pos[1]<=targetY[1] and pos[1]>=targetY[0]:
        isHit=True
    else:
        if pos[1]<=targetY[0]:
            if pos[0]>2*targetX[1]:
                isLong=True
            else:
                isShort=True
    return(isHit,isLong,isShort)

pos =[0,0]
vel0=[0,0]
velHitSet=set();

# sweep potential velocity range, fast enough to just guess bounds
for Vy0 in range(-200,200):
    done=False
    cnt=0;

    while not done:
        cnt+=1
        vel=[vel0[0]+cnt, Vy0]
        pos=[0,0]
        velStart=vel.copy()
        isHit  = False
        isShort= False
        isLong = False
        posYmax=0
        velYmax=[0,0]
        # propagate trajectory until it's Long/Short or Hits
        while (not (isHit or isLong or isShort)):
            pos,vel = step(pos,vel)
            # Track max height
            if pos[1]>posYmax:
                posYmax=pos[1];
                velYmax = velStart
            isHit,isLong,isShort = inTarget(pos,vel)

        # If we hit target, record max height and corresponding initial velocity
        # Add Vo to set of initial velocities
        if isHit:
            velHitSet.add((velStart[0],velStart[1]))
            posYmaxValid = posYmax
            velYmaxValid = velYmax
            #print("   Hit at {} with Vo:{} and max {}".format(pos,velStart,posYmaxValid))

        # Once we are long, stop incrementing initial Vx, move to test next Vy
        if isLong:
            done=True

print("The answer to Part A is {0:d}".format(posYmaxValid))
print("The answer to Part B is {0:d}".format(len(velHitSet)))

