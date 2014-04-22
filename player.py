from __future__ import division
from visual import*
import math

class player():
    def __init__(self):
        self.value = 0
        self.score = label(pos=(-350,350,0), text='Score: %d' % self.value)
        self.incremented = False

    def incrementScore(self):
        self.value = self.value + 1
        self.score = label(pos=(-350,350,0), text='Score: %d' % self.value)



#include player in obstacle
#add 'p1.incremented = False to obstacle movement if statement
#create new if statement in obstacle with same condition but past 0 and incremented False
#inside, increment score and set incremented to True
