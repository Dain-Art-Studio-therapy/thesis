from vector_math import *
from data import *
import utility


def sphere_intersection_point(ray,sphere):
    a = dot_vector(ray.dir, ray.dir)

    bdiff = difference_point(ray.pt, sphere.center)
    bdotvec = dot_vector(bdiff, ray.dir)
    b = 2 * bdotvec

    cdiff1  = difference_point(ray.pt, sphere.center)
    cdotvec = dot_vector(cdiff1, cdiff1)
    cradsq  = sphere.radius ** 2
    c = cdotvec - cradsq

    disc = (b ** 2) - (4 * a * c)
    if disc >= 0:
        t1 = ((-b + math.sqrt(disc)) / (2*a))
        t2 = ((-b - math.sqrt(disc)) / (2*a))
        pointt1 = translate_point(ray.pt, scale_vector(ray.dir, t1))
        pointt2 = translate_point(ray.pt, scale_vector(ray.dir, t2))
        if t1 >=0 and t2 >= 0:
            if t1 < t2:
                return pointt1
            else:
                return pointt2
        elif t1 >= 0:
            return pointt1
        elif t2 >= 0:
            return pointt2
        else:
            return None


def find_intersection_points(sphere_list, ray):

    # list = []
    # for sphere in sphere_list:
    #     point = sphere_intersection_point(ray, sphere)
    #     if point:
    #         tuple = (sphere, point)
    #         list.append(tuple)
    # return list

    return [(sphere, sphere_intersection_point(ray, sphere)) for sphere in sphere_list if sphere_intersection_point(ray, sphere) != None]


def sphere_normal_at_point(sphere,point):

    return normalize_vector(vector_from_to(sphere.center, point))