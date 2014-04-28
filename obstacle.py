from __future__ import division
from visual import*
from bird import*
from player import*
import math
import random

#variable to store how large the gap is
gap = 250
#a constant
m = 1/2
#varialbe to store how large the started axis is
axisStart = 375

#class obstacle
class obstacle():
    #default 
    def __init__(self,x):
        #top and bot are both cylinders
        self.top = cylinder(pos=(x,500,0),axis=(0,-axisStart,0),radius=45,color=color.green,material=materials.wood)
        self.bot = cylinder(pos=(x,-500,0),axis=(0,axisStart,0),radius=45,color=color.green,material=materials.wood)

    #collision detection
    def detection(self,bird):
        check = True
        vector1 = bird.ball.pos-self.top.pos
        vector2 = bird.ball.pos-self.bot.pos
        
        #length from the position of an obstacle to its corner
        c1=sqrt(self.top.radius**2+(self.top.axis.y)**2)
        c2=sqrt(self.bot.radius**2+(self.bot.axis.y)**2)
        
        #checking starts at here
        #check if the ball goes into the checking area
        if abs(vector1.x)<=self.top.radius+bird.ball.radius:
            #check if the ball is between the checking area and the edge of a cyliner
            if abs(vector1.x)>self.top.radius:
                #check if the ball is touching the edge of cylinders
                if bird.ball.pos.y>=self.top.pos.y-self.top.axis.y or bird.ball.pos.y<=self.bot.pos.y+self.bot.axis.y:
                    check = False
                #check if the ball touches the corner
                elif mag(vector1)<c1+bird.ball.radius or mag(vector2)<c2+bird.ball.radius:
                    check = False
            #check if the ball goes in the area of the gap
            elif abs(vector1.x)<=2*self.top.radius:
                #check if the ball touches either one end of the cylinders
                if abs(abs(vector1.y)-bird.ball.radius)<=abs(self.top.axis.y) or abs(abs(vector2.y)-bird.ball.radius)<=self.bot.axis.y:
                    check = False
        return check

    #function moves the obstacle and deal with the score increment
    def moveObstacle(self,dt,Vx,sceneRange,p1):
        #uniform linear motion to the left
        self.top.pos.x=self.top.pos.x-Vx*dt
        self.bot.pos.x=self.bot.pos.x-Vx*dt
        
        #check if the obstacles goes out of the boundary of the scree, if so put them back to the right of the screen
        #and call modifyGap function to move the gap between cylinders;
        #also set the p1.incremented False
        if self.top.x+self.top.radius<-sceneRange:
            self.modifyGap(sceneRange)
            self.top.x=sceneRange+self.top.radius
            self.bot.x=sceneRange+self.bot.radius
            p1.incremented = False
        
        #check if it's supposed to increment the score
        if self.top.x+self.top.radius<0 and p1.incremented == False:
            p1.incrementScore()
            p1.incremented = True

    #function moves the gap's position between the cylinders
    def modifyGap(self,screenRange): 
        #generate a random integer between 1 and screen-1 for changing the length of the top cylinder
        r = random.randint(1,screenRange-1) 
        #calculate the length for the bot cylinder
        rest = screenRange - r + gap
        #undate both cylinders
        self.top.axis.y = -r 
        self.bot.axis.y = rest
        


    

