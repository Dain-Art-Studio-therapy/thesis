import math
from data import*
from vector_math import *

def sphere_intersection_point(ray,sphere):   
    A=dot_vector(ray.dir,ray.dir)
    B=(2*(ray.pt-sphere.center)*ray.dir)
    C=((ray.pt-sphere.center)**2-sphere.radius**2)
    Square_root_of_Discriminant=math.sqrt(B**2-4*A*C)   
    pointy1 = (-B+Square_root_of_Discriminant) / (2.0*A) #because point t sounds like pointy
    pointy2 = (-B-Square_root_of_Discriminant) / (2.0*A)

    if math.sqrt(B**2-4*A*C)<0 or (pointy1<0 and pointy2<0):
        return None
    elif math.sqrt(B**2-4*A*C)==0:
        pointy=-B/(2.0*A)
        return translate_point(ray.pt, (scale_vector(ray.dir, pointy)))
    else:
        if pointy1 >= 0 and pointy2 >= 0:
            return translate_point(ray.pt, (scale_vector(ray.dir, min(pointy1, pointy2))))
        elif pointy1 >= 0:
            return translate_point(ray.pt, (scale_vector(ray.dir, pointy1)))
        else:
            return translate_point(ray.pt, (scale_vector(ray.dir, pointy2)))


def find_intersection_points(ray,sphere_list):
    l=[]
    for sphere in sphere_list:
        if point is not None:
            l.append(sphere,point)
    return l

def sphere_normal_at_point(sphere,point):
    vft=vector_from_to(sphere.center,point)
    return normalize_vector(vft)
