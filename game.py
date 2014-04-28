from __future__ import division
from visual import*
from obstacle import*
from bird import*
from player import*
import math

#create variables to serve as a reference for the scene dimensions
#(since we can't reference scene.range, only set it)
sceneRange = 500
sceneWidth = 500

#set the scene dimensions based on the variables created above
scene.range = sceneRange
scene.width = sceneWidth

#set the scene not to change the view as objects enter, leave, or move on the scene
scene.autoscale = 0

#set the title of the window
scene.title = 'Flappy Bird!'

#handle when user presses arrow key{
def keyInput(keyIn):
    #as long as the bird has not collided with anything
    if obs1.detection(b1) == True:
        #and if the key pressed is up or space
        if (keyIn.key == 'up' or keyIn.key == ' '):
            b1.jump()
        #if the key pressed is enter/return
        if keyIn.key == '\n':
            #remove the start game prompt and start the game
            startLabel.visible = False
            StartGame()
            #if the current achieved score is greater than the saved highscore
            if p1.value>temp:
                #replace the highscore, cast it to a string, and write over the old highscore
                highscore=p1.value
                highscore=str(highscore)
                fileO.write(highscore)
            #if the saved highscore is still the highest
            else:
                #write it back to the highscore file
                highscore=temp
                highscore=str(temp)
                fileO.write(highscore)
            #close the file
            fileA.close()
            fileI.close()
            fileO.close()
#}

#when the user presses a key, go to key handler function
scene.bind('keydown', keyInput)

#prompt the game to start, called from keyInput on enter/return press
#begins the while loop that handles all of the movement of the objects over time
def StartGame():
    #while the bird has not collided with anything or hit the ground
    while obs1.detection(b1) == True and obs2.detection(b1) == True and b1.bottom == False:
        #move the bird according to its velocity and move the obstacles across the screen
        b1.moveBird(dt)
        obs1.moveObstacle(dt,Vx,500,p1)
        obs2.moveObstacle(dt,Vx,500,p1)
        rate(1000)

#open file to read highscore
fileA = open("highscore.txt","a+")
fileI = open("highscore.txt","r")

#attempt to read from the highscore file, if it exists
try:
    highscore=fileI.read()
    #if there was no highscore to read, initialize to 0
    if highscore=='':
        highscore='0'
    #cast highscore to an integer, since it is read as a string
    highscore=int(highscore)
#if the highscore file does not exist, intitialize highscore to 0
except IOError:
    highscore=0

#create a temporary variable to hold and compare highscore
temp = highscore

#open file to write highscore
fileO = open("highscore.txt","w")

#create highscore label in bottom left
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

#draw the start game prompt label
startLabel = label(pos=(0,0,0),text='Press Enter to start!')



