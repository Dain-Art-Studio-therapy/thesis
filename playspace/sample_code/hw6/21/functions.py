import math

def scale_value(c):
   min_value = 0.2
   if c < 0.2:
      return min_value
   else:
      return c
   
def scalar(radius, dist):
   return (radius - dist) / (radius)
   
def square(x):
   return x ** 2
   
def distance(x1, x2, y1, y2, z1, z2):
   return math.sqrt(square(x1 - x2) + square(y1 -y2) +
          square(z1 - z2))

def get_color(c, row_x, x1, col_y, y1, z, z1, radius):
   return int(scale_value(abs(scalar(radius, 
          distance(row_x, x1, col_y, y1, z, z1)))) * c)

