from __future__ import division
from visual import*
from bird import*
from player import*
import math
import random

gap = 250
m = 1/2
axisStart = 375
class obstacle():
    #default 
    def __init__(self,x):
        self.top = cylinder(pos=(x,500,0),axis=(0,-axisStart,0),radius=45,color=color.green,material=materials.wood)
        self.bot = cylinder(pos=(x,-500,0),axis=(0,axisStart,0),radius=45,color=color.green,material=materials.wood)

    #collision detection
    def detection(self,bird):
        check = True
        vector1 = bird.ball.pos-self.top.pos
        vector2 = bird.ball.pos-self.bot.pos
        
        #length of the center of an obstacle to a corner
        c1=sqrt(self.top.radius**2+(self.top.axis.y)**2)
        c2=sqrt(self.bot.radius**2+(self.bot.axis.y)**2)
        
        if abs(vector1.x)<=self.top.radius+bird.ball.radius:
            if abs(vector1.x)>self.top.radius:
                if bird.ball.pos.y>=self.top.pos.y-self.top.axis.y or bird.ball.pos.y<=self.bot.pos.y+self.bot.axis.y:
                    check = False
                    print '1'
                #elif c1-bird.ball.radius<mag(vector1)<c1+bird.ball.radius or c2-bird.ball.radius<mag(vector2)<c2+bird.ball.radius:
                elif mag(vector1)<c1+bird.ball.radius or mag(vector2)<c2+bird.ball.radius:
                    check = False
                    print '2'
            elif abs(vector1.x)<=2*self.top.radius:
                if abs(abs(vector1.y)-bird.ball.radius)<=abs(self.top.axis.y) or abs(abs(vector2.y)-bird.ball.radius)<=self.bot.axis.y:
                    check = False
                    print '3'
        return check

    #movement
    def moveObstacle(self,dt,Vx,sceneRange,p1):
        self.top.pos.x=self.top.pos.x-Vx*dt
        self.bot.pos.x=self.bot.pos.x-Vx*dt
        if self.top.x+self.top.radius<-sceneRange:
            self.modifyGap(sceneRange)
            self.top.x=sceneRange+self.top.radius
            self.bot.x=sceneRange+self.bot.radius
            p1.incremented = False
        if self.top.x+self.top.radius<0 and p1.incremented == False:
            p1.incrementScore()
            p1.incremented = True

    #change gap
    def modifyGap(self,screenRange): 
        r = random.randint(1,screenRange-1) 
        rest = screenRange - r + gap
        self.top.axis.y = -r 
        self.bot.axis.y = rest
        


    

