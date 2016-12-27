import vector_math
import math

def sphere_intersection_point(ray, sphere):
	a = vector_math.dot_vector(ray.dir, ray.dir)
	b = vector_math.dot_vector(vector_math.scale_vector((vector_math.difference_point(ray.pt, sphere.center)), 2), ray.dir)
	c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius**2
	if (b**2 - 4 * a * c < 0): return None
	t0 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	t1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	if (t0 >= 0 and t1 >= 0):
		point0 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t0))
		point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
		if (vector_math.length_vector(vector_math.vector_from_to(point0, ray.pt)) < vector_math.length_vector(vector_math.vector_from_to(point1, ray.pt))): return point0
		else: return point1
	elif (t0 >= 0): return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t0))
	elif (t1 >= 0): return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
	else: return None
	
def find_intersection_points(sphere_list, ray):
	pairs = []
	for x in sphere_list:
		temp_point = sphere_intersection_point(ray, x)
		if (temp_point is not None): pairs.append((x, temp_point))
	return pairs
	
def sphere_normal_at_point(sphere, point):
	return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
