import math
import data
import vector_math


def sphere_intersection_point(ray,sphere):
    a = vector_math.dot_vector(ray.dir, ray.dir)

    bdiff = vector_math.difference_point(ray.pt, sphere.center)
    bdotvec = vector_math.dot_vector(bdiff, ray.dir)
    b = 2 * bdotvec

    cdiff  = vector_math.difference_point(ray.pt, sphere.center)
    cdotvec = vector_math.dot_vector(cdiff, cdiff)
    cradsquare  = sphere.radius ** 2
    c = cdotvec - cradsquare

    disc = (b**2) - (4*a*c)

    if disc >= 0:
        t1 = ((-b + math.sqrt(disc)) / (2*a))
        t2 = ((-b - math.sqrt(disc)) / (2*a))
        pt1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
        pt2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))

        if t1 >=0 and t2 >= 0:
            if t1 < t2:
                return pt1
            else:
                return pt2
        elif t1 >= 0:
            return pt1
        elif t2 >= 0:
            return pt2
        else:
            return None


def find_intersection_points(sphere_list,ray):
    return[(sphere, sphere_intersection_point(ray, sphere)) for sphere in sphere_list if sphere_intersection_point(ray, sphere) != None]



def sphere_normal_at_point(sphere,point):
    return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))
