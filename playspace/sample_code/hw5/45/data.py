import utility

class Finish:
    def __init__(self,ambient,diffuse,specular,roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness
    def __eq__(self,other):
        return utility.epsilon_equal(self.ambient,other.ambient) and utility.epsilon_equal(self.diffuse,other.diffuse) and utility.epsilon_equal(self.specular,other.specular) and utility.epsilon_equal(self.roughness,other.roughness)

class Light:
    def __init__(self,pt,color):
        self.pt = pt
        self.color = color
    def __eq__(self,other):
        return utility.epsilon_equal(self.pt.x,other.pt.x) and utility.epsilon_equal(self.pt.y,other.pt.y) and utility.epsilon_equal(self.pt.z,other.pt.z) and utility.epsilon_equal(self.color.r,other.color.r) and utility.epsilon_equal(self.color.g,other.color.g) and utility.epsilon_equal(self.color.b,other.color.b)

class Color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self,other):
        return utility.epsilon_equal(self.r,other.r) and utility.epsilon_equal(self.g, other.g) and utility.epsilon_equal(self.b,other.b)

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
    def __init__(self,pt,d):
        self.pt = pt
        self.d = d
    def __eq__(self,other):
        return utility.epsilon_equal(self.pt.x,other.pt.x) and utility.epsilon_equal(self.pt.y,other.pt.y) and utility.epsilon_equal(self.pt.z,other.pt.z) and utility.epsilon_equal(self.d.x,other.d.x) and utility.epsilon_equal(self.d.y,other.d.y) and utility.epsilon_equal(self.d.z,other.d.z)

class Sphere:
    def __init__(self,center,radius,color,finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self,other):
        return utility.epsilon_equal(self.center.x,other.center.x) and utility.epsilon_equal(self.center.y,other.center.y) and utility.epsilon_equal(self.center.z,other.center.z) and utility.epsilon_equal(self.radius,other.radius) and utility.epsilon_equal(self.color.r,other.color.r) and utility.epsilon_equal(self.color.g,other.color.g) and utility.epsilon_equal(self.color.b, other.color.b) and utility.epsilon_equal(self.finish.ambient,other.finish.ambient) and utility.epsilon_equal(self.finish.diffuse,other.finish.diffuse)
