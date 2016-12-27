from collisions import*
from data import *
from vector_math import *
import math



def shading(sphere,pt,ambientColor,light,sphere_list,eye_point):
	norm = sphere_normal_at_point(sphere, pt)
	PE = translate_point(pt, scale_vector(N,0.01))
	Ldir = normalize_vector(vector_from_to(PE,light.pt))
	ShadowColor = (sphere.color.r * sphere.finish.ambient * ambientColor.r, 
			sphere.color.g * sphere.finish.ambient * ambientColor.g, 
			sphere.color.b * sphere.finish.ambient * ambientColor.b)
	colorfromlight = Color(0, 0, 0)
	specularcolor = Color(0, 0, 0)

	if dot_vector(N, L_dir) > 0:
		if not find_intersection_points(sphere_list, Ray(PE, Ldir)):
			l_dot_norm = dot_vector(norm, Ldir)
			colorFromLight = Color(l_dot_norm * light.color.r * sphere.color.r * sphere.finish.diffuse, 
					l_dot_norm * light.color.g * sphere.color.g * sphere.finish.diffuse, 
					l_dot_norm * light.color.b * sphere.color.b * sphere.finish.diffuse)
			reflection = difference_vector(Ldir, scale_vector(N, 2 * l_dot_norm))
			V_dir = normalize_vector(vector_from_to(eye_point, PE))
			specularIntensity = dot_vector(reflection, Vect_dir)
			if specularIntensity > 0:
				specularColor = Color(light.color.r * sphere.finish.specular * specularIntensity**(1.0/sphere.finish.roughness), 
						light.color.g * sphere.finish.specular * specularIntensity**(1.0/sphere.finish.roughness), 
						light.color.b * sphere.finish.specular * specularIntensity**(1.0/sphere.finish.roughness))

	return Color(shadowColor.r + colorFromLight.r + specularColor.r, 
		shadowColor.g + colorFromLight.g + specularColor.g, 
		shadowColor.b + colorFromLight.b + specularColor.b)

def cast_ray(ray, sphere_list, ambientColor, eye_point):
	 color = Color(1.0, 1.0, 1.0)
	 points = find_intersection_points(sphere_list, ray)
	
	 if points:
			closest = length_vector(difference_point(points[0][1], ray.pt))
			color = shading(points[0][0], points[0][1], ambientColor, sphere_list, eye_point)

			for point in points:
				 length = length_vector(difference_point(point[1], ray.pt))
				 if length < closest:
						closest = length
						color = shading(point[0], point[1], ambientColor, light,sphere_list, eye_point)

	 return color

