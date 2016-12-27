import vector_math
import math
import data

def sphere_intersection_point(ray,sphere):
    
    A = vector_math.dot_vector(ray.dir,ray.dir)
    B = 2 *(vector_math.dot_vector(vector_math.vector_from_to(sphere.center,ray.pt),ray.dir))
    C = vector_math.dot_vector(vector_math.vector_from_to(sphere.center,ray.pt),vector_math.vector_from_to(sphere.center,ray.pt)) - sphere.radius ** 2
    d = B ** 2 - 4 * A * C
    d >= 0

    if d < 0:
        return None    
    t1 = (-1 * B + (math.sqrt(d))) / (2 * A)
    t2 = (-1 * B - (math.sqrt(d))) / (2 * A)
    
    if t1 == t2 or A == 0:
        return None
    
    if t1 > 0 and t2 > 0:
        if t1 > t2:
            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t2))
        else:
            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t1))
    elif t1 > 0 or t2 > 0:
        if t1 > 0:
            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t1))
        else:
            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t2))
    else:
        return None


def find_intersection_points(sphere_list, ray):
    list1 = []
    for i in range (0, len(sphere_list)):
        int_pt = sphere_intersection_point(ray, sphere_list[i])
        if int_pt != None:
            sp_and_int_pt = (sphere_list[i],int_pt)
            list1.append(sp_and_int_pt)
    return list1


def sphere_normal_at_point(sphere, point):
    vector = vector_math.vector_from_to(sphere.center,point)
    return vector_math.normalize_vector(vector)
    
    
