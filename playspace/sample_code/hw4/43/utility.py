__author__ = 'Aaron Keen'

import math
import data

# returns a boolean if two numbers are within
# epsilon distance from each other
def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

# calculates the distance from pt1 to pt2
def distance(pt1, pt2):
    return math.sqrt((pt2.x - pt1.x)**2
                     + (pt2.y - pt1.y)**2
                     + (pt2.z - pt1.z)**2)

# takes the internal color code (0.0 -> 1.0)
# and converts it to external color code (0 -> 255)
def convert_color(color):
    r = color.r * 255
    g = color.g * 255
    b = color.b * 255
    return data.Color(min(r, 255), min(g, 255), min(b, 255))

def color_mult(color1, color2):
    r = color1.r * color2.r
    g = color1.g * color2.g
    b = color1.b * color2.b
    return data.Color(r, g, b)

def color_scale(color, scalar):
    r = color.r * scalar
    g = color.g * scalar
    b = color.b * scalar
    return data.Color(r, g, b)

def color_add(color1, color2):
    r = color1.r + color2.r
    g = color1.g + color2.g
    b = color1.b + color2.b
    return data.Color(r, g, b)