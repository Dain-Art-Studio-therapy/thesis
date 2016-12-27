from utility import epsilon_equal

class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __eq__(self,other):
        return epsilon_equal(self.x,other.x) and epsilon_equal(self.y,other.y) and epsilon_equal(self.z,other.z)




class Ray:
    def __init__(self,pt,dir):
        self.pt=pt
        self.dir=dir
    def __eq__(self,other):
        return (self.pt.x == other.pt.x) and (self.pt.y == other.pt.y) and (self.pt.z == other.pt.z) and (self.dir.x == other.dir.x) and (self.dir.y == other.dir.y) and (self.dir.z == other.dir.z)




class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __eq__(self,other):
        return epsilon_equal(self.x,other.x) and epsilon_equal(self.y,other.y) and epsilon_equal(self.z,other.z)


class Sphere:
    def __init__(self,center,radius,color,finish):
        self.center=center
        self.radius=radius
        self.color=color
        self.finish=finish


    def __eq__(self,other):
        return (self.center.x == other.center.x) and (self.center.y == other.center.y) and (self.center.z == other.center.z) and epsilon_equal(self.radius,other.radius) and epsilon_equal(self.color.r,other.color.r) and epsilon_equal(self.color.g,other.color.g) and epsilon_equal(self.color.b,self.other.b) and (self.finish.ambient==other.finish.ambient) and (self.finish.diffuse==other.finish.diffuse) and (self.finish.specular==other.finish.specular) and (self.finish.specular==other.finish.specular)




class Color:
   def __init__(self,r,g,b):
       self.r=r
       self.g=g
       self.b=b

   def __eq__(self,other):
        return epsilon_equal(self.r,other.r) and (self.g,other.g) and (self.b,other.b)


class Finish:
    def __init__(self,ambient,diffuse,specular,roughness):
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
        self.roughness=roughness



    def __eq__(self,other):
        return epsilon_equal(self.ambient,other.ambient) and epsilon_equal(self.diffuse,other.diffuse) and epsilon_equal(self.specular,other.specular) and epsilon_equal(self.roughness,other.roughness)


class Light:
    def __init__(self,point,color):
        self.point=point
        self.color=color



    def __eq__(self,other):
        return (self.center.x == other.center.x) and (self.center.y == other.center.y) and (self.center.z == other.center.z) and (self.color.r ==self.color.r) and (self.color.g ==self.color.g) and (self.color.b ==self.color.b)