from __future__ import division
from visual import*
from obstacle import*
from bird import*
from player import*
import math

#set the screen window size
sceneRange = 500
sceneWidth = 500
scene.range = sceneRange
scene.width = sceneWidth
scene.autoscale = 0
scene.title = 'Flappy Bird!'

#create ball
b1=bird()

#create pipe obstacles
obs1=obstacle(sceneRange)
obs2=obstacle(sceneRange*2)
#obs2=cylinder(pos=(150,-150,0),axis=(0,150,0),radius=75/2,color=color.green)

#create obstacle velocity constants
dt=.01
Vx=25

#create player and draw score
p1=player()

startLabel = label(pos=(0,0,0),text='Press Enter to start!')

#handle when user presses arrow key{
def keyInput(keyIn):
    if obs1.detection(b1) == True:
        if (keyIn.key == 'up' or keyIn.key == 'space'):#if UP and the ball is not at the top of the screen, can move
            b1.jump()
            #print 'jumped'
        if keyIn.key == '\n':
            startLabel.visible = False
            StartGame()
#}
        
scene.bind('keydown', keyInput)#when the user presses a key, go to key handler function


def StartGame():
    while obs1.detection(b1) == True and obs2.detection(b1) == True and b1.bottom == False:
        b1.moveBird(dt)
        obs1.moveObstacle(dt,Vx,500,p1)
        obs2.moveObstacle(dt,Vx,500,p1)
        rate(1000)

#moveObs(obs1,b1,dt,Vx)
#moveObs(obs2,b1,dt,Vx)


