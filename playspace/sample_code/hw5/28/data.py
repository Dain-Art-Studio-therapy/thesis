import utility
class Finish:
	def __init__(self,ambient,diffuse, specular, roughness):
		self.ambient = ambient 
		self.diffuse = diffuse
		self.specular = specular
		self.roughness = roughness
	def __eq__(self, other):
		return (utility.epsilon_equal(self.ambient,other.ambient)
			and utility.epsilon_equal(self.diffuse,other.diffuse)
			and utility.epsilon_equal(self.specular,other.specular)
			and utility.epsilon_equal(self.roughness,other.roughness))
class Light:
	def __init__(self,point,color):
		self.point = point
		self.color = color
	def __eq__(self, other):
		return self.point==other.point and self.color==other.color
class Color:
	def __init__(self,r,g,b):
		self.r = r # internal colors
		self.g = g 
		self.b = b 
	def __str__(self): # external colors
		if self.r < 1.0:
			r = int(self.r*255)
		else:
			r = 255
		if self.g < 1.0:
			g = int(self.g*255)
		else:
			g = 255
		if self.b < 1.0:
			b = int(self.b*255)
		else:
			b = 255
		return str(r) + ' '+ str(g) + ' ' + str (b) #string-ify
	def __eq__(self, other):
		return (utility.epsilon_equal(self.r,other.r) 
			and utility.epsilon_equal(self.g,other.g) 
			and utility.epsilon_equal(self.b,other.b))
class Point:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __eq__(self, other):
		return (utility.epsilon_equal(self.x,other.x) 
			and utility.epsilon_equal(self.y,other.y) 
			and utility.epsilon_equal(self.z,other.z))
class Vector:
	def __init__(self,x,y,z):
		self.x = x 
		self.y = y 
		self.z = z 
	def __eq__(self, other):
		return (utility.epsilon_equal(self.x,other.x) 
			and utility.epsilon_equal(self.y,other.y) 
			and utility.epsilon_equal(self.z,other.z))

class Ray:
	def __init__(self,pt,dir, color):
		self.pt = pt
		self.dir = dir
		self.color = color
	def __eq__(self, other):
		return (self.pt==other.pt and self.dir==other.dir
			and self.color==other.color)

class Sphere:
	def __init__(self,center,radius,color,finish):
		self.center = center
		self.radius = radius
		self.color = color
		self.finish = finish
	def __eq__(self, other):
		return (self.center==other.center and self.radius==other.radius
			and self.color==other.color and self.finish==other.finish)

