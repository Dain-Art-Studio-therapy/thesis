import unittest
from data import *

def scale_vector(vector,scalar):
    return Vector(vector.vx*scalar, vector.vy*scalar, vector.vz*scalar)

def dot_vector(vect1,vect2):
    return ((vect1.vx*vect2.vx) + (vect1.vy*vect2.vy) + (vect1.vz*vect2.vz))

def length_vector(vect):
    return ((vect.vx**2)+(vect.vy**2)+(vect.vz**2))**0.5

def normalize_vector(vector):
    length = length_vector(vector)
    return Vector(vector.vx/length,vector.vy/length,vector.vz/length)

def difference_point(point1,point2):
    ptx = point1.x - point2.x
    pty = point1.y - point2.y
    ptz = point1.z - point2.z
    return Vector(ptx,pty,ptz)
    
def difference_vector(vector1,vector2):
    Vectx = vector1.vx - vector2.vx
    Vecty = vector1.vy - vector2.vy
    Vectz = vector1.vz - vector2.vz
    return Vector(Vectx,Vecty,Vectz)
    
def translate_point(point,vector):
    ptx = point.x + vector.vx
    pty = point.y + vector.vy
    ptz = point.z + vector.vz
    return Point(ptx,pty,ptz)

def vector_from_to(from_point,to_point):
    VecX = to_point.x - from_point.x
    VecY = to_point.y - from_point.y
    VecZ = to_point.z - from_point.z
    return Vector(VecX,VecY,VecZ)