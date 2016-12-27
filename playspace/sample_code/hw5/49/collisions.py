import data
from vector_math import *
import math

# The quadratic function
def quadratic_plus(A, B, C):
	return (-B + math.sqrt(B**2 - 4*A*C)) / (2 * A)

def quadratic_minus(A, B, C):
	return (-B - math.sqrt(B**2 - 4*A*C)) / (2 * A)

def sphere_intersection_point(ray, sphere):
	A = dot_vector(ray.dir, ray.dir)
	B = dot_vector(
		scale_vector(difference_point(ray.pt, sphere.center), 2),
		ray.dir)
	C = (dot_vector(
			difference_point(ray.pt, sphere.center),
			difference_point(ray.pt, sphere.center))
	     - sphere.radius ** 2)

	dis = B**2 - 4*A*C # discriminant
	if dis < 0: # no root
		return None
	else:
		quad_plus = quadratic_plus(A, B, C)
		quad_minus = quadratic_minus(A, B, C)

	# two nonnegative roots
	if dis > 0 and quad_minus >= 0:
		return translate_point(ray.pt, 
				scale_vector(ray.dir, 
					quad_minus))
 
	# one nonnegative and one negative root
	elif dis > 0 and quad_minus < 0 and quad_plus >= 0:
		return translate_point(ray.pt, 
				scale_vector(ray.dir, 
					quad_plus))

	# one nonnegative root only
	elif dis == 0 and quad_minus >= 0:
		return translate_point(ray.pt, 
				scale_vector(ray.dir, 
					quad_plus))

	else: # two negative roots, one negative root only
		return None

def find_intersection_points(sphere_list, ray):
	result = []
	for sphere in sphere_list:
		if sphere_intersection_point(ray, sphere) is not None:
			result.append((sphere,
				       sphere_intersection_point(ray, sphere)))
	return result

def sphere_normal_at_point(sphere, point):
	if point is not None:
		return normalize_vector(vector_from_to(sphere.center, point))

