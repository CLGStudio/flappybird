from __future__ import division
from visual import*
#from obstacle import*
import math
#import Image

class bird():
    def __init__(self):
        self.ball = sphere(pos=(0,0,0),radius=30, color=color.red)
        self.ball.velocity = vector(0,0,0)
        self.bottom = False
        self.jumpSteps = 50
        #self.maxVy = 100

        #self.pos = (0,0,0)
        #self.radius = 30
        #self.color = color.red

    def moveBird(self, dt):
        self.ball.velocity.y = self.ball.velocity.y - 9.8*dt
        self.ball.pos = self.ball.pos + (0,self.ball.velocity.y*dt,0)
        if self.ball.pos.y < -450:
            self.bottom = True
            print 'hit bottom'
        
    def jump(self):
        if self.ball.pos.y > 500:
            self.ball.pos.y = 500
        else:
            self.ball.velocity.y = self.jumpSteps
