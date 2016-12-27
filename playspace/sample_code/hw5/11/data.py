from utility import *
class Point:
      def __init__(self,x, y, z):
           self.x = x
           self.y = y
           self.z = z
      def __eq__(self, other):
           return epsilon_equal(self.x,other.x) and \
 epsilon_equal(self.y,other.y) and epsilon_equal(self.z, other.z)
class Vector:
     def  __init__(self, x, y, z):
           self.x = x
           self.y = y
           self.z = z
     def __eq__(self, other):
           return epsilon_equal(self.x, other.x) and \
 epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)
class Ray:
     def __init__(self, pt, dir):
          self.pt = pt
          self.dir = dir
     def __eq__(self, other):
          return self.pt == other.pt and self.dir == other.dir

class Sphere:
     def __init__(self, center, radius,color, finish):
          self.center = center
          self.radius = radius
          self.color = color
          self.finish = finish
     def __eq__(self, other):
          return self.center == other.center and \
 epsilon_equal(self.radius, other.radius)

class Color:
     def __init__(self, r, g, b):
          self.r = r
          self.g = g
          self.b = b
     def __eq__(self,other):
          return epsilon_equal(self.r,other.r) and \
 epsilon_equal(self.g,other.g) and epsilon_equal(self.b,other.b)
     def __mul__(self,other):
          return Color(self.r*other.r,self.g*other.g,self.b*other.b)
     def color_scalar(self,val):
          return Color(self.r * val, self.g * val, self.b * val)
     def __add__(self,other):
          return Color(self.r+other.r,self.g+other.g,self.b+other.b)

class Finish:
     def __init__(self,ambient, diffuse, specular, roughness):
          self.ambient = ambient
          self.diffuse = diffuse
          self.specular = specular
          self.roughness = roughness
     def __eq__(self,other):
          return self.ambient == other.ambient and self.diffuse == other.diffuse and self.specular == \
 other.specular and self.roughness == other.roughness

class Light:
     def __init__(self, pt, color):
          self.pt = pt
          self.color = color
     def __eq__(self, other):
          return self.pt == other.pt and self.color == other.color
