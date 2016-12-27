import data
import vector_math
import utility
import math

def sphere_intersection_point(ray,sphere):

    dif = vector_math.difference_point(ray.pt,sphere.center)
    
    A = vector_math.dot_vector(ray.dir,ray.dir) 
    B = vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt, sphere.center),2), ray.dir)
    C = vector_math.dot_vector(dif, dif) - (sphere.radius ** 2)

    #Computes discriminate
    d = B ** 2 - (4 * A * C)

    if d < 0:
        #No real roots
        return None
    else:
        #Some possible roots
        if d == 0:
            #one root
            t = -B / (2 * A)
            pointT = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir,t))
        elif d > 0:
            #two real roots
            t = (-B + math.sqrt(B ** 2 - (4 * A * C))) / (2 * A)
            t2 = (-B - math.sqrt(B ** 2 - (4 * A * C))) / (2 * A)

            if t < 0 and t2 < 0:
                return None
            elif t > 0 and t2 > 0:
                if t > t2:
                    pointT =  vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir,t2))
                    return pointT
                else:
                    pointT = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir,t))
                    return pointT
            elif t > 0 and t2 < 0:
                pointT = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir,t))
                return pointT
            else:
                pointT = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir,t2))
                return pointT

def find_intersection_point(sphere_list,ray):
    return [(x, sphere_intersection_point(ray, x)) for x in sphere_list if sphere_intersection_point(ray, x) != None]

def sphere_normal_at_point(sphere,point):
    return vector_math.normalize_vector(vector_math.difference_point(point, sphere.center))
