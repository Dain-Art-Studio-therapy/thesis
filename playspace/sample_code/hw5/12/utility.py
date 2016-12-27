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
    r = color.r * 255.0
    g = color.g * 255.0
    b = color.b * 255.0
    return data.Color(int(min(r, 255.0)), int(min(g, 255.0)), int(min(b, 255.0)))

# takes two colors and multiplies their r, g, b values together
def color_mult(color1, color2):
    r = color1.r * color2.r
    g = color1.g * color2.g
    b = color1.b * color2.b
    return data.Color(r, g, b)

# takes a color and scales its r, g, b value
def color_scale(color, scalar):
    r = color.r * float(scalar)
    g = color.g * float(scalar)
    b = color.b * float(scalar)
    return data.Color(r, g, b)

# takes two colors and adds their r, g, b values together
def color_add(color1, color2):
    r = color1.r + color2.r
    g = color1.g + color2.g
    b = color1.b + color2.b
    return data.Color(r, g, b)