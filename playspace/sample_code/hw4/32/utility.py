import math
from data import *

def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

def distance(pt1, pt2):
   return math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2 + 
   (pt1.z - pt2.z)**2)

def mod_color(c1, c2):
   return Color(c1.r*c2.r, c1.g*c2.g, c1.b*c2.b)

def scale_color(color, scalar):
   return Color(color.r * scalar, 
   color.g * scalar,
   color.b * scalar)

def add_color(color, plus):
   return Color(color.r+plus, color.g+plus, color.b+plus)

def add_two_colors(c1, c2):
   return Color(c1.r+c2.r, c1.g+c2.g, c1.b+c2.b)

def cap_value(num):
   if num > 1.0:
      num = 1.0
   return num
