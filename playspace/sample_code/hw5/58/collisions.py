import math
import data
import vector_math

def discriminant(A, B, C):
   return (B ** 2 - (4 * A * C))

def pos_quad_formula(A, B, C):
   return (((-B) + math.sqrt(discriminant(A, B, C))) / (2 * A))

def neg_quad_formula(A, B, C):
   return (((-B) - math.sqrt(discriminant(A, B, C))) / (2 * A))

def sphere_intersection_point(ray, sphere):
   d = discriminant(vector_math.dot_vector(ray.dir, ray.dir), 
		    vector_math.dot_vector(vector_math.scale_vector
                      (vector_math.difference_point(ray.pt, sphere.center), 2),
                      ray.dir), 
		    (vector_math.dot_vector(vector_math.difference_point
                      (ray.pt, sphere.center), vector_math.difference_point
                      (ray.pt, sphere.center)) - sphere.radius ** 2))

   if d < 0:
        return None

   elif d > 0:
	pos_t = pos_quad_formula(vector_math.dot_vector(ray.dir, ray.dir), 
                     vector_math.dot_vector(vector_math.scale_vector
                       (vector_math.difference_point(ray.pt, sphere.center), 2),
                       ray.dir), 
		     (vector_math.dot_vector(vector_math.difference_point
                       (ray.pt, sphere.center), vector_math.difference_point
                       (ray.pt, sphere.center)) - sphere.radius ** 2))

	neg_t = neg_quad_formula(vector_math.dot_vector(ray.dir, ray.dir), 
                     vector_math.dot_vector(vector_math.scale_vector
                       (vector_math.difference_point(ray.pt, sphere.center), 2),
                       ray.dir), 
		     (vector_math.dot_vector(vector_math.difference_point
                       (ray.pt, sphere.center), vector_math.difference_point
                       (ray.pt, sphere.center)) - sphere.radius ** 2))

	if pos_t < 0 and neg_t < 0:
           return None

        elif pos_t >= 0 and neg_t < 0:
           new_point = vector_math.translate_point(ray.pt,
                       vector_math.scale_vector(ray.dir, pos_t))
	   return new_point

	elif neg_t >= 0 and pos_t < 0:
	   new_point = vector_math.translate_point(ray.pt,
                       vector_math.scale_vector(ray.dir, neg_t))
	   return new_point

	elif neg_t >= 0 and pos_t >= 0:
	   point1 = vector_math.translate_point(ray.pt,
                    vector_math.scale_vector(ray.dir, neg_t))
	   point2 = vector_math.translate_point(ray.pt,
                    vector_math.scale_vector(ray.dir, pos_t))
	   if abs(neg_t) > abs(pos_t):
              return point2
           else:
              return point1


def find_intersection_points(sphere_list, ray):
   new_list = []
   for e in sphere_list:
        intersection = sphere_intersection_point(ray, e)
      	if intersection is not None:
	   new_list.append((e, intersection))
   return new_list

def sphere_normal_at_point(sphere, point):
   normal = vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
   return normal
