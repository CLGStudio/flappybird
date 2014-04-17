from __future__ import division
from visual import*
from bird import*
from player import*
import math
import random

gap = 125
m = 1/2
class obstacle(cylinder):
    #default 
    def __init__(self,screenWidth,screenRange):
        self.top = cylinder(pos=(screenWidth,m*screenRange,0),axis=(0,screenRange,0),radius=m*75,color=color.green)
        self.bot = cylinder(pos=(screenWidth,-screenRange,0),axis=(0,250,0),radius=m*75,color=color.green)

    #collision detection
    def detection(self,bird):
        check = True
        vector1 = bird.ball.pos-(self.top.pos + (0,m*self.top.axis.y,0))
        vector2 = bird.ball.pos-(self.bot.pos + (0,m*self.bot.axis.y,0))
        #length of the center of an obstacle to a corner
        c1=sqrt(self.top.radius**2+(m*self.top.axis.y)**2)
        c2=sqrt(self.bot.radius**2+(m*self.bot.axis.y)**2)
        if abs(vector1.x)<=self.top.radius+bird.ball.radius:
            if abs(vector1.x)>self.top.radius:
                if bird.ball.pos.y>=self.top.pos.y or bird.ball.pos.y<=self.bot.pos.y+self.bot.axis.y:
                    check = False
                    print '1'
                #elif c1-bird.ball.radius<mag(vector1)<c1+bird.ball.radius or c2-bird.ball.radius<mag(vector2)<c2+bird.ball.radius:
                elif mag(vector1)<c1+bird.ball.radius or mag(vector2)<c2+bird.ball.radius:
                    check = False
                    print '2'
            elif abs(vector1.x)<=self.top.radius*2:
                if abs(abs(vector1.y)-bird.ball.radius)<=m*self.top.axis.y or abs(abs(vector2.y)-bird.ball.radius)<=m*self.bot.axis.y:
                    check = False
                    print '3'
        return check

    #movement
    def moveObstacle(self,dt,Vx,sceneRange,p1):
        self.top.pos.x=self.top.pos.x-Vx*dt
        self.bot.pos.x=self.bot.pos.x-Vx*dt
        if self.top.x+self.top.radius<-sceneRange:
            #self.modifyGap(sceneRange)
            self.top.x=sceneRange+self.top.radius
            self.bot.x=sceneRange+self.bot.radius
            p1.incremented = False
        if self.top.x+self.top.radius<0 and p1.incremented == False:
            p1.incrementScore()
            p1.incremented = True
        

    #change gap
    def modifyGap(self,screenRange):
        r=(screenRange-gap)*random.random()
        rest=screenRange-r-gap
        self.top.axis.y=2*r
        self.bot.axis.y=2*rest
        


    
