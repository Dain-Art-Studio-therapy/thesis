from utility import *
class Vector:
        def __init__(self,x,y,z):
                self.x = x
                self.y = y
                self.z = z
        def __eq__(self, other):
                return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

class Point:
        def __init__(self,x,y,z):
                self.x = x
                self.y = y
                self.z = z
        def __eq__(self,other):
                return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

class Ray:
        def __init__(self,pt,dir):
                self.pt = pt
                self.dir = dir
                self.pt.x = pt.x
                self.pt.y = pt.y
                self.pt.z = pt.z
                self.dir.x = dir.x
                self.dir.y = dir.y
                self.dir.z = dir.z
                
        def __eq__(self,other):
                return self.pt == other.pt and self.dir == other.dir
class Sphere:
        def __init__(self,center,radius,color,finish):
                self.center = center
                self.radius = radius
                self.color = color
                self.finish = finish
        def __eq__(self,other):
                return self.center == other.center and self.radius == other.radius and self.finish == other.finish

class Color:
        def __init__(self,R,G,B):
                self.r = R
                self.g = G
                self.b = B
        def __eq__(self,other):
                return epsilon_equal(self.r,other.r) and epsilon_equal(self.g, other.g) and epsilon_equal(self.b, other.b)

class Finish:
        def __init__(self,ambient,diffuse,specular,roughness):
                self.ambient = ambient
                self.diffuse = diffuse
                self.specular = specular
                self.roughness = roughness
        def __eq__(self,other):
                return self.ambient == other.ambient and self.diffuse == other.diffuse and self.roughness == other.roughness
class Light:
        def __init__(self,point,color):
                self.point = point
                self.color = color
        def __eq__(self,other):
                return self.point == other.point and self.color == other.color


