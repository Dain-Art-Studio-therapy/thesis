from utility import *

class Point:
   def __init__(self, x, y, z):
      self.x = x # all 3 are numbers
      self.y = y
      self.z = z
   def __eq__(self, other):
      return (epsilon_eq(self.x, other.x)
         and epsilon_eq(self.y, other.y)
         and epsilon_eq(self.z, other.z))

class Vector:
   def __init__(self, x, y, z):
      self.x = x # all 3 are numbers
      self.y = y
      self.z = z
   def __eq__(self, other):
      return (epsilon_eq(self.x, other.x)
         and epsilon_eq(self.y, other.y)
         and epsilon_eq(self.z, other.z))

class Ray:
   def __init__(self, pt, dir):
      self.pt = pt # point
      self.dir = dir # vector
   def __eq__(self, other):
      return (self.pt == other.pt
         and self.dir == other.dir)

class Sphere:
   def __init__(self, center, radius, color, finish):
      self.center = center # point
      self.radius = float(radius) # number
      self.color = color
      self.finish = finish
   def __eq__(self, other):
      return (self.center == other.center
         and epsilon_eq(self.radius, other.radius)
         and self.color == other.color
         and self.finish == other.finish)


class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
   
   def __eq__(self, other):
      return (epsilon_eq(self.r, other.r) and
              epsilon_eq(self.g, other.g) and
              epsilon_eq(self.b, other.b))
              
              
              
class Finish:
   def __init__(self, ambient, diffuse, specular, roughness):
      self.ambient = ambient
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness
      
   def __eq__(self, other):
      return (epsilon_eq(self.ambient, other.ambient) and
              epsilon_eq(self.diffuse, other.diffuse) and
              epsilon_eq(self.specular, other.specular) and
              epsilon_eq(self.roughness, other.roughness))
             
class Light:
   def __init__(self, pt, color):
      self.pt = pt
      self.color = color
      
   def __eq__(self, other):
      return self.pt == other.pt and self.color == other.color
