# Contains class definitions with __init__ functions
from utility import *

class Point:
   def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
   def __eq__(self, other):
      return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

class Vector:
   def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
   def __eq__(self, other):
      return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

class Ray:
   def __init__(self,pt,dir):
      self.pt=pt
      self.dir=dir
   def __eq__(self, other):
      return epsilon_equal(self.pt, other.pt) and epsilon_equal(self.dir, other.dir)

class Sphere:
   def __init__(self,center,radius):
      self.center=center
      self.radius=radius
   def __eq__(self, other):
      return epsilon_equal(self.center, other.center) and epsilon_equal(self.radius, other.radius)
