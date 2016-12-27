# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09

import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self,other):
        return utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y)

def distance(p1,p2):
    return math.sqrt(((p1.x - p2.x)**2) + ((p1.y - p2.y)**2))
