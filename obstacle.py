from __future__ import division
from visual import*
from bird import*
import math
import random

gap = 125
m = 1/2
dt=1
Vx=1
class obstacle(cylinder):
    #default 
    def __init__(self,screenWidth,screenRange):
        self.top = cylinder(pos=(m*screenWidth,m*screenRange,0),axis=(0,175,0),radius=m*75,color=color.green)
        self.bot = cylinder(pos=(m*screenWidth,-m*screenRange,0),axis=(0,175,0),radius=m*75,color=color.green)

    #collision detection
    def detection(self,bird):
        check = True
        vector1 = bird.pos-self.top.pos
        vector2 = bird.pos-self.bot.pos
        #length of the center of an obstacle to a corner
        c1=sqrt(self.top.radius**2+self.top.axis.y**2)
        c2=sqrt(self.bot.radius**2+self.bot.axis.y**2)
        if abs(vector1.x)<=self.top.radius+bird.radius:
            if abs(vector1.x)>self.top.radius:
                if bird.pos.y>=self.top.pos.y-m*top.axis.y or bird.pos<=self.bot.pos.y+m*self.bot.axis.y:
                    check = False
                elif c1-bird.radius<mag(vector1)<c1+bird.radius or c2-r<mag(vector2)<c2+bird.radius:
                    check = False
            else:
                if abs(abs(vector1.y)-bird.radius)<=m*self.top.axis.y or abs(abs(vector2.y)-bird.radius)<=m*self.bot.axis.y:
                    check = False
        return check

    #movement
    def moveObstacle(self):
        top.pos.x=top.pos.x-Vx*dt
        bot.pos.x=bot.pos.x-Vx*dt
        if top.x+2*top.radius<-m*mag(scene.range):
            modifyGap()
            top.x=mag(scene.range)*m+top.radius
            bot.x=mag(scene.range)*m+bot.radius
        

    #change gap
    def modifyGap(self):
        r=(screen.range-gap)*random.random()
        rest=screen.range-r-gap
        self.top.axis.y=2*r
        self.bot.axis.y=2*rest
        


    

