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

#handle when user presses arrow key{
def keyInput(keyIn):
    if obs1.detection(b1) == True:
        if (keyIn.key == 'up' or keyIn.key == 'space'):#if UP and the ball is not at the top of the screen, can move
            b1.jump()
            #print 'jumped'
        if keyIn.key == '\n':
            startLabel.visible = False
            StartGame()
            if p1.value>temp:
                highscore=p1.value
                highscore=str(highscore)
                fileO.write(highscore)
            else:
                highscore=temp
                highscore=str(temp)
                fileO.write(highscore)
            fileA.close()
            fileI.close()
            fileO.close()
#}

        
scene.bind('keydown', keyInput)#when the user presses a key, go to key handler function


def StartGame():
    while obs1.detection(b1) == True and obs2.detection(b1) == True and b1.bottom == False:
        b1.moveBird(dt)
        obs1.moveObstacle(dt,Vx,500,p1)
        obs2.moveObstacle(dt,Vx,500,p1)
        rate(1000)

#open file to load highscores and prepare to write
fileA = open("highscore.txt","a+")
fileI = open("highscore.txt","r")

try:
    highscore=fileI.read()
    if highscore=='':
        highscore='0'
    highscore=int(highscore)
except IOError:
    highscore=0
    
temp = highscore
print temp

fileO = open("highscore.txt","w")

#create highscore label
highLabel = label(pos=(-350,-350,0), text='Highscore: %d' % temp, box = False)

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



