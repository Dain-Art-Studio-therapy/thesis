import utility
class Color:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

    def __eq__(self,other):
        return self.r==other.r and self.g==other.g and self.b==other.b


class Finish:
    def __init__(self,ambient,diffuse,specular,roughness):
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
        self.roughness=roughness

    def __eq__(self,other):
        return self.ambient==other.ambient and self.diffuse==other.diffuse and self.specular==other.specular and self.roughness==other.roughness


class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __eq__(self,other):
        return(utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y, othey.y) and utility.epsilon_equal(self.z,other.z))


class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __eq__(self,other):
        return(utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y) and utility.epsilon_equal(self.z,other.z))  


class Ray:
    def __init__(self,pt,dir):
        self.pt=pt
        self.dir=dir
    def __eq__(self,other):
        return self.pt==other.pt and self.dir==other.dir


class Sphere:
    def __init__(self,center,radius,color, finish):
        self.center=center
        self.radius=radius
        self.color=color
        self.finish=finish

    def __eq__(self,other):
        return self.center==other.center and self.radius==other.radius


class Light:
    def __init__(self,pt,color):
        self.pt=pt
        self.color=color 

    def __eq__(self,other):
        return self.pt==other.pt and self.color==other.color


