from utility import *
class Point:
   def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self,other):
      return (epsilon_equal(self.x,other.x) 
          and epsilon_equal(self.y,other.y) 
          and epsilon_equal(self.z,other.z)) 


class Vector:
   def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self,other):
      return (epsilon_equal(self.x,other.x) 
       and epsilon_equal(self.y,other.y) 
       and epsilon_equal(self.z,other.z)) 

class Ray:
   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir
   def __eq__(self,other):
      return (epsilon_equal(self.pt.x,other.pt.x)
          and epsilon_equal(self.pt.y,other.pt.y)
          and epsilon_equal(self.pt.z,other.pt.z) 
          and  Vector.__eq__(self.dir, other.dir))
          
class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
   def __eq__(self,other):
      return (epsilon_equal(self.r, other.r) 
          and epsilon_equal(self.g,other.g)
          and epsilon_equal(self.b,other.b)) 

class Sphere:
   def __init__(self, center, radius, color, finish):
      self.center = center
      self.radius = radius
      self.color = color
      self.finish = finish
   def __eq__(self,other):
      return (Point.__eq__(self.center, other.center) 
       and epsilon_equal(self.radius,other.radius)
       and Color.__eq__(self.color,other.color)
       and Finish.__eq__(self.finish,other.finish)) 

class Finish:
    def __init__(self, ambience, diffuse, specular, roughness):
      self.ambience = ambience
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness
    def __eq__(self,other):
    	return (epsilon_equal(self.ambience, other.ambience) and 
  	      epsilon_equal(self.diffuse, other.diffuse) and
          epsilon_equal(self.specular, other.specular) and
          epsilon_equal(self.roughness, other.roughness))

class Light:
   def __init__(self, pt, color):
      self.pt = pt
      self.color = color
   def __eq__(self,other):
      return (Point.__eq__(self.pt, other.pt)
         and Color.__eq__(self.color, other.color))
