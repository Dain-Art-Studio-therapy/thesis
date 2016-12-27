import data
import math

def scale_vector(vector1, scalar):
        newvector = data.Vector(vector1.x, vector1.y, vector1.z)
        newvector.x = scalar * newvector.x
        newvector.y = scalar * newvector.y
        newvector.z = scalar * newvector.z
        return newvector

def dot_vector(v1,v2):
        return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def length_vector(v1):
        return math.sqrt((v1.x**2) + (v1.y**2) +(v1.z**2))

def normalize_vector(vector):
        vlength = length_vector(vector)
        newx = vector.x/vlength
        newy = vector.y/vlength
        newz = vector.z/vlength
        newvector = data.Vector(newx, newy, newz)
        return newvector

def difference_point(p1,p2):
        newVector = data.Vector(p1.x-p2.x,p1.y-p2.y,p1.z-p2.z)
        return newVector

def difference_vector(v1,v2):
        newVector = data.Vector(v1.x-v2.x, v1.y-v2.y, v1.z-v2.z)
        return newVector

def translate_point(point,vector):
        newx = point.x+vector.x
        newy = point.y+vector.y
        newz = point.z+vector.z
        newpoint = data.Point(newx, newy, newz)
        return newpoint

def vector_from_to(from_vector, to_vector):
        newvector = data.Vector(to_vector.x-from_vector.x, to_vector.y-from_vector.y, to_vector.z-from_vector.z)
        return newvector


