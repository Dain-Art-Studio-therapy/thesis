import data
import vector_math
import math


def sphere_intersection_points(ray, sphere):
    # returns a point if intersection if not then return None
    a = (vector_math.dot_vector(ray.dirs, ray.dirs))
    b = (
        vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt, sphere.center), 2),
                               ray.dirs))
    c0 = vector_math.difference_point(ray.pt, sphere.center)
    c1 = vector_math.dot_vector(c0, c0)
    c2 = sphere.radius ** 2
    c = (c1 - c2)
    d = ((b ** 2) - (4 * a * c))
    if d < 0:
        return None
    t1 = (-b + math.sqrt(d)) / (2.0 * a)
    t2 = (-b - math.sqrt(d)) / (2.0 * a)
    if t1 >= 0 and t2 >= 0:
        if t1 < t2:
            p0 = vector_math.scale_vector(ray.dirs, t1)
            p = vector_math.translate_point(ray.pt, p0)
            return p
        else:
            p0 = vector_math.scale_vector(ray.dirs, t2)
            p = vector_math.translate_point(ray.pt, p0)
            return p
    elif t1 >= 0 and t2 < 0:
        p0 = vector_math.scale_vector(ray.dirs, t1)
        p = vector_math.translate_point(ray.pt, p0)
        return p
    elif t2 >= 0 and t1 < 0:
        p0 = vector_math.scale_vector(ray.dirs, t2)
        p = vector_math.translate_point(ray.pt, p0)
        return p


def find_intersection_point(sphere_list, ray):
    newlist = []
    for sp in sphere_list:
        if sphere_intersection_points(ray, sp) is not None:
            newlist.append((sp, sphere_intersection_points(ray, sp)))
    return newlist

    # returns tuples where the ray and spheres intersect(sphere,point)


def sphere_normal_at_point(sphere, point):
    v = vector_math.difference_point(sphere.center, point)
    vnorm = vector_math.normalize_vector(v)
    return vnorm
