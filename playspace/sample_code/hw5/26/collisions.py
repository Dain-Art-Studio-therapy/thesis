import vector_math
import math

def sphere_intersection_point(ray, sphere):
    A = vector_math.dot_vector(ray.dir, ray.dir)
    B = 2*vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir)
    C = (vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), \
        vector_math.difference_point(ray.pt, sphere.center)) - sphere.rad**2)
    determinant = B*B - 4*A*C
 
    if determinant < 0 or A == 0:
         return None
    else:   
         t_value_0 = (-B + math.sqrt(determinant))/(2*A)
         t_value_1 = (-B - math.sqrt(determinant))/(2*A)

    if t_value_0 is None: 
        if t_value_1 < 0:
            return None
        else:
            return vector_math.translate_point(ray.pt, \
            vector_math.scale_vector(ray.dir, t_value_1))

    elif t_value_1 is None:
        if t_value_0 < 0:
            return None
        else:
            return vector_math.translate_point(ray.pt, \
                vector_math.scale_vector(ray.dir, t_value_0))

    elif t_value_0 < 0 and t_value_1 < 0:
        return None
    elif t_value_0 < 0:
        return vector_math.translate_point(ray.pt, \
            vector_math.scale_vector(ray.dir, t_value_1))
    elif t_value_1 < 0: 
        return vector_math.translate_point(ray.pt, \
            vector_math.scale_vector(ray.dir, t_value_0))
    elif t_value_0 < t_value_1:
        return vector_math.translate_point(ray.pt, \
            vector_math.scale_vector(ray.dir, t_value_0))
    else:
        return vector_math.translate_point(ray.pt, \
            vector_math.scale_vector(ray.dir, t_value_1)) 
          
     

def find_intersection_points(sphere_list, ray):
    intersection_pts = []
    for s in sphere_list:
        if sphere_intersection_point(ray, s) is not None:
            intersection_pts.append((s, sphere_intersection_point(ray, s)))
    return intersection_pts



# the following function uses these functions from vector_math:
   # vector_from_to(from_point, to_point)
   # normalize_vector(vector) 
def sphere_normal_at_point(sphere, point):
    return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,
       point))



  
