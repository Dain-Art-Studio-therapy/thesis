import utility


class Point():
    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and utility.epsilon_equal(self.z, other.z)
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z
    
class Vector():
    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and utility.epsilon_equal(self.z, other.z)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Ray:
    def __eq__(self, other):
        return utility.epsilon_equal(self.pt.x, other.pt.x) and utility.epsilon_equal(self.pt.y, other.pt.y) and utility.epsilon_equal(self.pt.z, other.pt.z) and utility.epsilon_equal(self.dir.x, other.dir.x) and utility.epsilon_equal(self.dir.y, other.dir.y) and utility.epsilon_equal(self.dir.z, other.dir.z) 
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

class Sphere:
     def __eq__(self, other):
          return utility.epsilon_equal(self.radius, other.radius) and self.center == other.center and self.color == other.color and self.finish == other.finish
     def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius 
        self.color = color
        self.finish = finish

class Color: 
    def __eq__(self,other):
        return utility.epsilon_equal(self.r, other.r) and utility.epsilon_equal(self.g, other.g) and utility.epsilon_equal(self.b, other.b)

    def __init__(self,r , g, b):
        self.r = r
        self.g = g
        self.b = b
class Finish: 
    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse) and utility.epsilon_equal(self.specular, other.specular) and utility.epsilon_equal(self.roughness, other.roughness)
    
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

class Light:
    def __eq__(self, other):
        return self.pt == other.pt and self.color == other.color 

    def __init__(self, pt, color):
        self.pt = pt
        self.color = color