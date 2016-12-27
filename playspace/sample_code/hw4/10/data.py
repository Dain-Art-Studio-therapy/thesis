from utility import *

class Point:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self, other):
      return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)    

class Vector:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self, other):
      return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

class Ray:
   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir
   def __eq__(self, other):
      return self.pt == other.pt and self.dir == other.dir

class Sphere:
   def __init__(self, center, radius, color, finish):
      self.center = center
      self.radius = radius
      self.color = color
      self.finish = finish
   def __eq__(self, other):
      return self.center == other.center and epsilon_equal(self.radius, other.radius) and self.color == other.color and self.finish == other.finish

class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
   def __eq__(self, other):
      return self.r == other.r and self.g == other.g and self.b == other.b

class Finish:
   def __init__(self, ambient, diffuse):
      self.ambient = ambient
      self.diffuse = diffuse
   def __eq__(self, other):
      return self.ambient == other.ambient and self.diffuse == other.diffuse

class Light:
   def __init__(self, position, intensity):
      self.position = position
      self.intensity = intensity
   def __eq__(self, other):
      return self.position == other.position and self.intensity == other.intensity
