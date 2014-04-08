from __future__ import division
from visual import*
import math
import obstacle
import bird

class bird(sphere):
    def _init_(self):
        self.ball = sphere(pos=(0,20,0),radius=30, color=color.red)

    def freeFall(self, dt):
        self.ball.velocity.y = vector(0,0,0)

        while 1:
            self.ball.pos = self.ball.pos + self.ball.velocity.y*dt
            self.ball.velocity.y = self.ball.velocity.y + (0,-9.8,0)*dt
            rate(100)
        
    def jump(self):
        if evt.key == 'space':
            self.ball.velocity.y = self.ball.velocity.y + (0,10,0)
