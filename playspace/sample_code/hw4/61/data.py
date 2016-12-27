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
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self,other):
        return utility.epsilon_equal(self.pt.x,other.pt.x) and utility.epsilon_equal(self.pt.y,other.pt.y) and utility.epsilon_equal(self.pt.z,other.pt.z) and utility.epsilon_equal(self.dir.x,other.dir.x) and utility.epsilon_equal(self.dir.y,other.dir.y) and utility.epsilon_equal(self.dir.z,other.dir.z)

class Sphere:
    def __init__(self,center,radius,color,finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish
       
    def __eq__(self,other):
        ctrx = utility.epsilon_equal(self.center.x,other.center.x)
        ctry = utility.epsilon_equal(self.center.y,other.center.y)
        ctrz = utility.epsilon_equal(self.center.z,other.center.z)
        radius = utility.epsilon_equal(self.radius,other.radius)
        return ctrx and ctry and ctrz and radius     

class Color:
    def __init__(self,r,g,b):
        self.r = r 
        self.g = g
        self.b = b

    def __eq__(self,other):
        r1 = utility.epsilon_equal(self.r,other.r) 
        g1 = utility.epsilon_equal(self.g,other.g)
        b1 = utility.epsilon_equal(self.b,other.b)
        return r1 and g1 and b1

class Finish:
    def __init__(self,ambient,diffuse,specular,roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self,other):
        amb = utility.epsilon_equal(self.ambient,other.ambient)
        diff = utility.epsilon_equal(self.diffuse,other.diffuse)
        spec = utility.epsilon_equal(self.specular,other.specular)
        rough = utility.epsilon_equal(self.roughness,other.roughness)
        return amb and diff and spec and rough

class Light:
    def __init__(self,pt,color):
        self.pt = pt
        self.color = color
    
    def __eq__(self,other):
        x = utility.epsilon_equal(self.pt.x,other.pt.x)
        y = utility.epsilon_equal(self.pt.y,other.pt.y)
        z = utility.epsilon_equal(self.pt.z,other.pt.z)
        r = utility.epsilon_equal(self.color.r,other.color.r)
        g = utility.epsilon_equal(self.color.g,other.color.g)
        b = utility.epsilon_equal(self.other.b,other.color.b)
        return x and y and z and r and g and b
