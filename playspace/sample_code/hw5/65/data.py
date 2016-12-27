# Han Tran || CPE 101-01,02 || Assisgnment 2
# Professor Keen

import utility

# POINT
class Point:
   def __init__(self, x, y, z):
       self.x = x
       self.y = y
       self.z = z
   
   def __eq__(self, other):
       return (utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and utility.epsilon_equal(self.z, other.z))



# VECTOR
class Vector:
   def __init__(self, x, y, z):
       self.x = x
       self.y = y
       self.z = z

   def __eq__(self, other):
       return (utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and utility.epsilon_equal(self.z, other.z))



# RAY
class Ray:
   def __init__(self, pt, dir):
       self.pt = pt
       self.dir = dir
   
   def __eq__(self, other):
       return (utility.epsilon_equal(self.pt.x, other.pt.x) and utility.epsilon_equal(self.pt.y, other.pt.y) and utility.epsilon_equal(self.pt.z, other.pt.z) and utility.epsilon_equal(self.dir.x, other.dir.x) and utility.epsilon_equal(self.dir.y, other.dir.y) and utility.epsilon_equal(self.dir.z, other.dir.z))


# SPHERE
class Sphere:
   def __init__(self, center, radius, color, finish):
       self.center = center
       self.radius = radius
       self.color = color
       self.finish = finish

   def __eq__(self, other):
       return (utility.epsilon_equal(self.center.x, other.center.x) and utility.epsilon_equal(self.center.y, other.center.y) and utility.epsilon_equal(self.center.z, other.center.z) and utility.epsilon_equal(self.radius, other.radius) and utility.epsilon_equal(self.color.r, other.color.r) and utility.epsilon_equal(self.color.g, other.color.g) and utility.epsilon_equal(self.color.b, other.color.b) and utility.epsilon_equal(self.finish.ambient, other.finish.ambient) and utility.epsilon_equal(self.finish.diffuse, other.finish.diffuse) and utility.epsilon_equal(self.finish.specular, other.finish.specular) and utility.epsilon_equal(self.finish.roughness, other.finish.roughness)) 


# Color
class Color:
   def __init__(self, r, g, b):
       self.r = r
       self.g = g
       self.b = b

   def __eq__(self, other):
       return(utility.epsilon_equal(self.r, other.r) and utility.epsilon_equal(self.g,other.g) and utility.epsilon_equal(self.b, other.b))


# Finish
class Finish:
   def __init__(self, ambient, diffuse, specular, roughness):
       self.ambient = ambient
       self.diffuse = diffuse
       self.specular = specular
       self.roughness = roughness


   def __eq__(self, other):
       return (utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse) and utility.epsilon_equal(self.specular, other.specular) and utility.epsilon_equal(self.roughness, other.roughness))


# Light
class Light:
   def __init__(self, pt, color):
       self.pt = pt
       self.color = color

   def __eq__(self, other):
       return (utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.color.r, other.color.r) and utility.epsilon_equal(self.color.g, other.color.g) and utility(self.color.b, other.color.b))

