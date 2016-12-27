import utility

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self,other):
        return utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y) and utility.epsilon_equal(self.z,other.z)
    
class Vector():
    def __init__(self, vx, vy, vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz
    def __eq__(self,other):
        return utility.epsilon_equal(self.vx,other.vx) and utility.epsilon_equal(self.vy,other.vy) and utility.epsilon_equal(self.vz,other.vz)

class Ray():
    def __init__(self, point, dir):
        self.point = point
        self.dir = dir
    def __eq__(self,other):
        return utility.epsilon_equal(self.point.x,other.point.x) and utility.epsilon_equal(self.point.y,other.point.y) and utility.epsilon_equal(self.point.z,other.point.z) and utility.epsilon_equal(self.dir.vx,other.dir.vx) and utility.epsilon_equal(self.dir.vy,other.dir.vy) and  utility.epsilon_equal(self.dir.vz,other.dir.vz)
    
class Sphere():
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish
    def __eq__(self,other):
        return utility.epsilon_equal(self.center.x,other.center.x) and utility.epsilon_equal(self.center.y,other.center.y) and utility.epsilon_equal(self.center.z,other.center.z) and utility.epsilon_equal(self.radius,other.radius) and utility.epsilon_equal(self.color.r,other.color.r) and utility.epsilon_equal(self.color.g,other.color.g) and utility.epsilon_equal(self.color.b,other.color.b) and utility.epsilon_equal(self.finish,other.finish)

class Color():
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self,other):
        return utility.epsilon_equal(self.r,other.r) and utility.epsilon_equal(self.g,other.g)and utility.epsilon_equal(self.b,other.b)

class Finish():
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness
    def __eq__(self,other):
        return utility.epsilon_equal(self.ambient,other.ambient) and utility.epsilon_equal(self.diffuse,other.diffuse) and utility.epsilon_equal(self.specular,other.specular) and utility.epsilon_equal(self.roughness,other.roughness)

class Light():
    def __init__(self, point, color):
        self.point = point
        self.color = color
    def __eq__(self,other):
        return utility.epsilon_equal(self.point.x,other.point.x) and utility.epsilon_equal(self.point.y,other.point.y) and utility.epsilon_equal(self.point.z,other.point.z) and utility.epsilon_equal(self.color.r,other.color.r) and utility.epsilon_equal(self.color.g,other.color.g) and utility.epsilon_equal(self.color.b,other.color.b)