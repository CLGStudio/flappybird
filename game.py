from __future__ import division
from visual import*
from obstacle import*
from bird import*
import math

#set the screen window size
scene.range = 500
scene.width = 500
scene.autoscale = 0

#create ball
b1=bird()

#create pipe obstacles
obs1=obstacle(500,500)
#obs2=cylinder(pos=(150,-150,0),axis=(0,150,0),radius=75/2,color=color.green)

#create obstacle velocity constants
dt=.5
Vx=25

#handle when user presses arrow key{
def keyInput(keyIn):
    if obs1.detection(b1) == True:
        if (keyIn.key == 'up' or keyIn.key == 'space'):#if UP and the ball is not at the top of the screen, can move
            b1.jump()
            print 'jumped'
#}
        
scene.bind('keydown', keyInput)#when the user presses a key, go to key handler function

#while no collision has been detected{
while obs1.detection(b1) == True and b1.bottom == False:
    sleep(.0001)
    b1.moveBird(dt)
    obs1.moveObstacle(dt,Vx,500)
    print 'r'
#}
