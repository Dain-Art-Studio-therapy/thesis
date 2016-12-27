import utility


class Point:
    def __init__(self,x,y,z):
       self.x = x
       self.y = y
       self.z = z

    def __eq__(self, other):
        x = utility.epsilon_equal(self.x, other.x, epsilon=0.00001)
        y = utility.epsilon_equal(self.y, other.y, epsilon=0.00001)
        z = utility.epsilon_equal(self.z, other.z, epsilon=0.00001)


class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        x = utility.epsilon_equal(self.x, other.x, epsilon=0.00001)
        y = utility.epsilon_equal(self.y, other.y, epsilon=0.00001)
        z = utility.epsilon_equal(self.z, other.z, epsilon=0.00001)



class Ray:
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        pt = self.pt == other.pt
        dir = self.dir == other.dir


class Sphere:
    def __init__(self,center,radius,color,finish):
        self.center = center
        self.radius = radius
        self.color = color

    def __eq__(self, other):
        center = self.center == other.center
        radius = utility.epsilon_equal(self.radius, other.radius, epsilon=0.00001)
        color = self.color == other.color
        finish = utility.epsilon_equal(self.finish, other.finish, epsilon= 0.0001)

    
class Color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        r = utility.epsilon_equal(self.r, other.r, epsilon=0.00001)
        g = utility.epsilon_equal(self.g, other.g, epsilon=0.00001)
        b = utility.epsilon_equal(self.b, other.b, epsilon=0.00001)


class Finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        ambient = utility.epsilon_equal(self.ambient, other.ambient, epsilon=0.00001)
        diffuse = utility.epsilon_equal(self.diffuse, other.diffuse, epsilon=0.00001)
        specular = utility.epsilon_equal(self.specular, other.specular, epsilon=0.00001)
        roughness = utility.epsilon_equal(self.roughness, other.roughness, epsilon=0.00001)

class Light:
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self,other):

        return (self.pt == other.pt and self.color == other.color)
