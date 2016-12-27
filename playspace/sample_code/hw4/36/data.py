import utility
class Point:

    def __init__(self,x,y,z):
       self.x=x
       self.y=y
       self.z=z

    def __eq__(self,other):
       return (utility.epsilon_equal(self.x, other.x) and
       utility.epsilon_equal(self.y, other.y) and
       utility.epsilon_equal(self.z,other.z))

class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __eq__(self,other):
        return (utility.epsilon_equal(self.x,other.x) and 
        utility.epsilon_equal(self.y,other.y) and
        utility.epsilon_equal(self.z,other.z))

class Ray:

    def __init__(self,pt,dir):
        self.pt=pt
        self.dir=dir

    def __eq__(self,other):
        return (utility.epsilon_equal(self.pt.x, other.pt.x) and
        utility.epsilon_equal(self.pt.y, other.pt.y) and 
        utility.epsilon_equal(self.pt.z, other.pt.z) and 
        utility.epsilon_equal(self.dir.x, other.dir.x) and 
        utility.epsilon_equal(self.dir.y, other.dir.y) and
        utility.epsilon_equal(self.dir.z, other.dir.z))
	
class Sphere:

    def __init__(self,center,radius,color, finish):
        self.center=center
        self.radius=radius
        self.color=color
        self.finish=finish

    def __eq__(self,other):
        return (utility.epsilon_equal(self.center.x, other.center.x) and 
        utility.epsilon_equal(self.center.y, other.center.y) and
        utility.epsilon_equal(self.center.z, other.center.z) and
        utility.epsilon_equal(self.radius,other.radius))

class Color:

    def __init__(self,r,g,b):
         self.r=r
         self.g=g
         self.b=b

    def __eq__(self,other):

        return (utility.epsilon_equal(self.r, other.r) and 
        utility.epsilon_equal(self.g, other.g) and
        utility.epsilon_equal(self.b, other.b))

class Finish:

    def __init__(self, ambient):
         self.ambient=ambient

    def __eq__(self,other):

         return (utility.epsilon_equal(self.ambient, other.ambient))