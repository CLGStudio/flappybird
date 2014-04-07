from __future__ import*
from visual import*
import math
import random
import bird

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
        vector1 = bird.pos-self.top.pos
        vector2 = bird.pos-self.bot.pos
        #length of the center of an obstacle to a corner
        c1=sqrt(self.top.r**2+self.top.axis.y**2)
        c2=sqrt(self.bot.r**r+self.bot.axis.y**2)
        if abs(vector1.x)<=top.radius+bird.radius:
            if abs(vector1.x)>top.radius:
                if bird.pos.y>=top.pos.y-m*top.axis.y or bird.pos<=bot.pos.y+m*bot.axis.y:
                    return False
                elif c1-bird.radius<mag(vector1)<c1+bird.radius or c2-r<mag(vector2)<c2+bird.radius:
                    return False
            else:
                if abs(abs(vector1.y)-bird.radius)<=m*top.axis.y or abs(abs(vector2.y)-bird.radius)<=m*bot.axis.y:
                    return False
         return True

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
        top.axis.y=2*r
        bot.axis.y=2*rest
        


    

