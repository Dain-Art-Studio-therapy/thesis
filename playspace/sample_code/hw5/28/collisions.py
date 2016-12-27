from data import *
import math
from vector_math import *
def sphere_intersection_point(ray, sphere):
	theSphere = sphere
	theRay = ray
	ray_pt_minus_sphere_center = difference_point(theRay.pt,theSphere.center)

	A = dot_vector(theRay.dir, theRay.dir)
	B = 2 * dot_vector(ray_pt_minus_sphere_center,theRay.dir)
	C = (dot_vector(ray_pt_minus_sphere_center, ray_pt_minus_sphere_center)
		 - theSphere.radius**2)
	discriminant=(B**2-4*A*C)

	if discriminant==0: #because then when square rooted the 
					#quatratic root formula is undifined
		root = -B/float(2*A)
		middle_step = scale_vector(theRay.dir, root)
		pointt = translate_point(theRay.pt, middle_step)
		if root>=0:
			return pointt

	elif discriminant > 0: # two roots
		sqrt_discrim = math.sqrt(discriminant)
		root1 = (-B + sqrt_discrim)/float(2*A)
		middle_step1 = scale_vector(theRay.dir, root1)
		pointt1 = translate_point(theRay.pt, middle_step1)

		root2 = (-B-sqrt_discrim)/float(2*A)
		middle_step2 = scale_vector(theRay.dir, root2)
		pointt2 = translate_point(theRay.pt, middle_step2)

		if root1>=0 and root2>=0:
			if root1<=root2:
				return pointt1
			else:
				return pointt2

		elif root1>=0 or root2>=0:
			if root1>=0:
				return pointt1
			else:
				return pointt2
		else:
			return None

	else:
		return None
#because then when square rooted the 
#quatratic root formula is undifined


def find_intersection_points(ray, sphere_list):
	found_pts=[]
	for sphere in sphere_list:
		if sphere_intersection_point(ray, sphere) is not None:
			sp_pt_tuple= (sphere, sphere_intersection_point(ray, sphere))
			found_pts.append(sp_pt_tuple)
	if found_pts==[]:
		return None
	else:
		return found_pts


def sphere_normal_at_point(sphere, point):
	from_point = sphere.center
	distance_vector = difference_point(point, from_point)
	dist_squared = square_vector(distance_vector)
	radius = sphere.radius
	if dist_squared == radius**2:
			norm_v= normalize_vector(distance_vector)
			return norm_v
	else:
		return None
