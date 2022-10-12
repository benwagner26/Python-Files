from vpython import *
from time import *

wallThickness = .1
roomWidth = 10
roomDepth = 10
roomHeight = 10
mRadius = .75
# First Marble
deltaZ = .1
deltaY = .1
deltaX = .1
xPos=1
yPos = 2
zPos = 3
# Second Marble
deltaZ2 = .1
deltaY2 = .1
deltaX2= .1
xPos2=3
yPos2= 2
zPos2 = 2
# Third Marble
deltaZ3 = .1
deltaY3 = .1
deltaX3= .1
xPos3=0
yPos3 = 0
zPos3 = 0



if mRadius*2 > roomHeight or mRadius*2 > roomWidth or mRadius*2 > roomDepth:
    print("Must make the ball diameter smaller than height, width, and depth of container")
    exit()


ceiling= box(pos=vector(0,roomHeight/2,0), size=vector(roomWidth, wallThickness,roomDepth))
floor = box(pos=vector(0,-roomHeight/2,0), color=color.white, size=vector(roomWidth, wallThickness,roomDepth))
leftWall = box(pos=vector(-roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
backWall = box(pos=vector(0,0,-roomDepth/2), color=color.white, size=vector(roomWidth,roomHeight,wallThickness))
rightWall = box(pos=vector(roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
marble1 = sphere(color=color.red, radius = mRadius)
marble2 = sphere(color=color.white, radius = mRadius)
marble3 = sphere(color=color.blue, radius = mRadius)

topEdge = roomHeight/2 - (mRadius + wallThickness)
bottomEdge = -roomHeight/2 + (mRadius + wallThickness)
backEdge = -roomDepth/2 + (mRadius + wallThickness)
frontEdge = roomDepth/2 - (mRadius + wallThickness)
rightEdge = roomWidth/2 - (mRadius + wallThickness)
leftEdge = -roomWidth/2 + (mRadius + wallThickness)


while True:
    rate(10)
    xPos+=deltaX
    yPos+=deltaY
    zPos+=deltaZ
    if (xPos > rightEdge or xPos < leftEdge):
        deltaX*=-1
    if (yPos > topEdge or yPos < bottomEdge):
        deltaY*=-1
    if (zPos > frontEdge or zPos < backEdge):
        deltaZ*=-1
    marble1.pos = vector(xPos, yPos, zPos)

    xPos2+=deltaX2
    yPos2+=deltaY2
    zPos2+=deltaZ2
    if (xPos2 > rightEdge or xPos2 < leftEdge):
        deltaX2*=-1
    if (yPos2 > topEdge or yPos2 < bottomEdge):
        deltaY2*=-1
    if (zPos2 > frontEdge or zPos2 < backEdge):
        deltaZ2*=-1
    marble2.pos = vector(xPos2, yPos2, zPos2)

    xPos3+=deltaX3
    yPos3+=deltaY3
    zPos3+=deltaZ3
    if (xPos3 > rightEdge or xPos3 < leftEdge):
        deltaX3*=-1
    if (yPos3 > topEdge or yPos3 < bottomEdge):
        deltaY3*=-1
    if (zPos3 > frontEdge or zPos3 < backEdge):
        deltaZ3*=-1
    marble3.pos = vector(xPos3, yPos3, zPos3)
