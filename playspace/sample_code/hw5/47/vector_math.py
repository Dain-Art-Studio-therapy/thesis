import math 
import data

def scale_vector(vector,scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    newVector = data.Vector(x,y,z)
    return newVector
 

def dot_vector(vector1,vector2):
      dotVector=(( (vector1.x * vector2.x) + (vector1.y * vector2.y) +
                (vector1.z * vector2.z)))

      # Test Case Purposes
      return dotVector 

def length_vector(vector):
      length = math.sqrt((vector.x ** 2) +( vector.y ** 2)+ (vector.z **2)) 
      # Test Case Purposes
      return length 

def normalize_vector (vector):
      length=length_vector(vector)
      x = vector.x/ length
      y = vector.y/ length
      z = vector.z/ length
      normal=data.Vector(x,y,z) 

      return normal
      
def difference_point(point1, point2):
      x = point1.x - point2.x
      y = point1.y - point2.y
      z = point1.z - point2.z
      newVec=data.Vector(x,y,z)
      return newVec

def difference_vector(vector1,vector2):
      x= vector1.x - vector2.x
      y= vector1.y - vector2.y
      z= vector1.z - vector2.z
      differenceVector=data.Vector(x,y,z)
      
      return differenceVector 

def translate_point(point,vector):
      x= point.x + vector.x
      y= point.y + vector.y
      z= point.z + vector.z
      translatePoint=data.Point(x,y,z)
      
      return translatePoint     

def vector_from_to(from_point,to_point):
      x= to_point.x - from_point.x
      y= to_point.y - from_point.y
      z= to_point.z - from_point.z
      newVec=data.Vector(x,y,z)
     
      return newVec






