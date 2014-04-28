from __future__ import division
from visual import*
import math

#create the player class
class player():
    #define the initialization method
    def __init__(self):
        #set the score (value) to zero, create the label which will display the score
        #and initialize the incremented flag to False (tracks when to increment score)
        self.value = 0
        self.score = label(pos=(-350,350,0), text='Score: %d' % self.value)
        self.incremented = False

    #define the increment score method
    #the 'incremented' flag is set from obstacle.py when the bird passes through a set of obstacles
    #(i.e. when the obstacles pass the middle of the scene)
    def incrementScore(self):
        #increment the score and update the display
        self.value = self.value + 1
        self.score = label(pos=(-350,350,0), text='Score: %d' % self.value)

