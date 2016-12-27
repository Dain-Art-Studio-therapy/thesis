# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

import vector_math
import math

def sphere_intersection_point(ray, sphere):
    # Description: determines if the given ray intersects the given sphere

    # Returns: The point of intersection - if there is no point of intersection,
    # None is returned

    # using quadratic formula
    A = vector_math.dot_vector(ray.dir, ray.dir)
    B = 2 * (vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir))
    C = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius**2

    # calculating discriminant
    disc = B ** 2 - 4 * A * C

    if disc < 0:
        pass
    elif disc == 0:
        # one root
        sol1 = -B / (2 * A)
        point_sol1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, sol1))

        if sol1 >= 0:
            return point_sol1
    else:
        # two roots
        sol1 = (-B + math.sqrt(disc)) /  (2 * A)
        sol2 = (-B - math.sqrt(disc)) / (2 * A)
        point_sol1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, sol1))
        point_sol2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, sol2))

        if sol1 >= 0 and sol2 >= 0:
            if sol1 < sol2:
                return point_sol1
            else:
                return point_sol2
        elif sol1 < 0 and sol2 > 0:
            return point_sol2
        elif sol1 > 0 and sol2 < 0:
            return point_sol1

def find_intersection_points(sphere_list, ray):
    # Description: Finds corresponding intersection points from a list
    # of spheres

    # Returns: A list of tuples with each tuple being (Sphere, Point)

    results = []

    for s in sphere_list:
        if sphere_intersection_point(ray, s) != None:
            results.append((s, sphere_intersection_point(ray, s)))

    return results

def sphere_normal_at_point(sphere, point):
    # Description: Finds the normal vector, which is the vector from the center
    # of the sphere to the point

    # Returns: A vector, the normal vector

    norm = vector_math.vector_from_to(sphere.center, point)
    return vector_math.normalize_vector(norm)
