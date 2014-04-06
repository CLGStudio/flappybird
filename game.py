from __future__ import division
from visual import*
import math
import obstacle
import bird


#set the screen window size
scene.range = 500
scene.width = 500
scene.autoscale = 0

#create ball
ball=sphere(pos=(0,-10,0),radius=30,color=color.red)

#create pipe obstacles
obs1=cylinder(pos=(150,150,0),axis=(0,150,0),radius=75/2,color=color.green)
obs2=cylinder(pos=(150,-150,0),axis=(0,150,0),radius=75/2,color=color.green)

#handle when user presses arrow key{
def keyInput(keyIn):
    if checkCollision(bird) == False:0
        if (keyIn.key == 'up' or keyIn.key == 'space') and ball.y < m*scene.width-r:#if UP and the ball is not at the top of the screen, can move
            ball.pos = ball.pos + (0,40,0)
#}
        
scene.bind('keydown', keyInput)#when the user presses a key, go to key handler function

#while no collision has been detected{
while checkCollision(bird) == False:
	#moveBird()
	#movePipes()
#}
