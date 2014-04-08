from __future__ import division
from visual import*
from obstacle import*
import math

class bird(sphere):
    def __init__(self):
        self.ball = sphere(pos=(0,0,0),radius=30, color=color.red)
        self.ball.velocity = vector(0,-20,0)
        self.bottom = False

    def moveBird(self, dt):
        self.ball.velocity.y = self.ball.velocity.y -9.8*dt
        self.ball.pos = self.ball.pos + (0,self.ball.velocity.y*dt,0)
        if self.ball.pos.y < -375:
            self.bottom = True
            print 'hit bottom'
        
    def jump(self):
        self.ball.velocity.y = self.ball.velocity.y + 70
