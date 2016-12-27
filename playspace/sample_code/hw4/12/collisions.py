from data import *
from vector_math import *
import math

def sphere_intersection_point(ray,sphere):
        a = dot_vector(ray.dir,ray.dir)
        b = 2*dot_vector(difference_point(ray.pt,sphere.center),ray.dir)
        c = (dot_vector(difference_point(ray.pt,sphere.center),difference_point(ray.pt,sphere.center)) - (sphere.radius**2))
        ##check for imaginary numbers##
        if ((b**2 - 4*a*c)) < 0:
                return None
        d1 = (-b + math.sqrt((b)**2 - 4*a*c))/(2*a)
        d2 = (-b - math.sqrt((b)**2 - 4*a*c))/(2*a)
        root = [d1,d2]
        if root[0] < 0 and root[1] <0:
                return None
        else:
                if root[0] <= root[1]:
                        t = root[0]
                elif root[0] > root[1]:
                        t = root[1]
                return translate_point(ray.pt,scale_vector(ray.dir,t))

def find_intersection_points(sphere_list, ray):
        L = []
        for i in range(len(sphere_list)):
                p = sphere_intersection_point(ray,sphere_list[i])
                if p != None:
                        newTup = (sphere_list[i],p)
                        L.append(newTup)
        return L

def sphere_normal_at_point(sphere,point):
        vec = difference_point(point,sphere.center)
        normal = normalize_vector(vec)
        return normal
