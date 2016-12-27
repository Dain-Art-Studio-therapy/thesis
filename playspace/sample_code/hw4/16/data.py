import utility

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self,other):
        return utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y) and utility.epsilon_equal(self.z,other.z)

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self,other):
        return utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y) and utility.epsilon_equal(self.z,other.z)

class Ray:
    def __init__(self,pt,drc): #expects a point (point object) and direction (vector object)
        self.pt = pt
        self.dir = drc
    def __eq__(self,other):
        return (self.pt == other.pt) and (self.dir == other.dir)

class Sphere:
    def __init__(self,c,r,col,fin): #expects a center (point object and a radius (float)
        self.center = c
        self.radius = r
        self.color = col
        self.finish = fin
    def __eq__(self,other):
        return (self.center == other.center) and (self.radius == other.radius) and (self.color == other.color)

class Color:
    def __init__(self,r,g,b): #24 bit color like it's 1999
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self,other):
        return utility.epsilon_equal(self.r,other.r) and utility.epsilon_equal(self.g,other.g) and utility.epsilon_equal(self.b,other.b)

class Finish:
    def __init__(self,ambient,diff,spec,rough):
        self.amb = ambient
        self.diff = diff #diffuse for the lazy
        self.spec = spec #specular
        self.rough = rough #roughness
    def __eq__(self,other):
        return self.color == other.color and self.diff == self.diff and self.spec == other.spec and self.rough == other.rough

class Light:
    def __init__(self,pt,color):
        self.pt = pt
        self.col = color
    def __eq__(self,other):
        return self.pt == other.pt and self.col == other.col

