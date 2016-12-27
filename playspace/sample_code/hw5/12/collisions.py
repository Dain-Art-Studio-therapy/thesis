__author__ = 'Jarrett'

import vector_math
import math
import data

# sphere_intersection_point returns the point where a ray
# intersects a sphere and if it intersects twice it chooses
# the first intersection
def sphere_intersection_point(ray, sphere):
    pt_to_center = vector_math.difference_point(ray.pt, sphere.center)

    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = (2 * vector_math.dot_vector(pt_to_center, ray.dir))
    c = vector_math.dot_vector(pt_to_center, pt_to_center) - sphere.radius**2

    determinant = (b**2 - (4 * a * c))

    if (determinant >= 0):
        t1 = (-b + math.sqrt(determinant)) / (2 * a)
        t2 = (-b - math.sqrt(determinant)) / (2 * a)

        if (t1 >= 0 and t2 >= 0):
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, min(t1, t2)))

        elif (t1 >= 0):
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))

        elif (t2 >= 0):
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))

        else:
            return None

    else:
        return None

# find_intersections_points takes the spheres from a list
# and finds all the intersection points the list has with a ray
# it returns a list of tuples with a sphere and a point
def find_intersection_points(sphere_list, ray):
    newlist = []

    for e in sphere_list:
        if (sphere_intersection_point(ray, e) != None):
            t = (e, sphere_intersection_point(ray, e))
            newlist.append(t)

    return newlist

# finds the direction (via unit vector) from the center
# of a sphere to a point on the sphere
def sphere_normal_at_point(sphere, point):
    radius_to_sphere = vector_math.vector_from_to(sphere.center, point)
    return vector_math.normalize_vector(radius_to_sphere)
