from __future__ import division
from visual import*
import math

class player():
    def __init__(self):
        self.value = 0
        self.score = label(pos=(-350,350,0), text='Score: %d' % self.value)

    def incrementScore(self):
        self.value = self.value + 1
        self.score = label(pos=(-350,350,0), text='Score: %d' % self.value)
