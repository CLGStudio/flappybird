from __future__ import division
from visual import*
#from obstacle import*
import math
#import Image

#creating gravity constant
gravity = 9.8
difficulty = 2
screenHeight = 500

class bird():
    def __init__(self):
        #creating ball and setting default values
        self.ball = sphere(pos=(0,0,0),radius=30, color=color.red)
        #setting default velocity
        self.ball.velocity = vector(0,0,0)
        self.bottom = False
        #how far the ball jumps
        self.jumpSteps = 70
        #self.maxVy = 100

        #self.pos = (0,0,0)
        #self.radius = 30
        #self.color = color.red

    #function to move bird at a constant downward velocity
    def moveBird(self, dt):
        #updating velocity of ball
        #the 2 is here to improve gaming experience/to make it a bit more difficult
        self.ball.velocity.y = self.ball.velocity.y - difficulty*gravity*dt
        #updating the ball's position with new velocity
        self.ball.pos = self.ball.pos + (0,self.ball.velocity.y*dt,0)
        #condition statement to check if ball hits the ground
        if self.ball.pos.y < -(screenHeight-50):
            self.bottom = True
            print 'hit bottom'
    #function to "jump"    
    def jump(self):
        #condition statement to check if ball is above the screen height. If it is set position to screen height.
        if self.ball.pos.y > screenHeight:
            self.ball.pos.y = screenHeight
        #set velocity = to the jumpsteps var.
        else:
            self.ball.velocity.y = self.jumpSteps
