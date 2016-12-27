import math
import unittest
from data import *
from collisions import *
from vector_math import *
import sys

##############################################################################

def specular_finder(g, ray, sphere_list, color, light, mindex):


        n = sphere_normal_at_point(g[mindex][0], g[mindex][1])
        pe = translate_point(g[mindex][1], scale_vector((n), (0.01)))
        ldir = normalize_vector(vector_from_to(pe, light.pt))
        ldotn = dot_vector(n, ldir)
        rr = (difference_vector(normalize_vector(vector_from_to(pe, light.pt)),  
	      scale_vector(n, 2 * dot_vector(n, ldir))))                      
        ep = Point(0.0, 0.0, -14.0)
        vdir = normalize_vector(vector_from_to(ep, pe))
        si = dot_vector(rr, vdir)
        if si > 0:
                return Color((light.color.r * g[mindex][0].finish.specular * 
			     (si ** (1/ g[mindex][0].finish.roughness))),
                             (light.color.g * g[mindex][0].finish.specular * 
			     (si ** (1/ g[mindex][0].finish.roughness))),
                             (light.color.b * g[mindex][0].finish.specular * 
			     (si ** (1/ g[mindex][0].finish.roughness))))
        else:
                return Color(0.0, 0.0, 0.0)



def diffuse_finder(g, sphere_list, ray, color, light, mindex):
	n = sphere_normal_at_point(g[mindex][0], g[mindex][1])
        pe = translate_point(g[mindex][1], scale_vector((n), (0.01)))
        ldir = normalize_vector(vector_from_to(pe, light.pt))
        dot = dot_vector(n, ldir)
	r = Ray(pe, ldir)
	ZZZ = sphere_intersection_point(r, g[mindex][0])
        XXX = find_intersection_points(sphere_list, r)
	SS = specular_finder(g, ray, sphere_list, color, light, mindex)
	
	if XXX != []:
		if (length_vector(vector_from_to(pe, XXX[0][1])) < 
		    length_vector(vector_from_to(pe, light.pt))):
			return Color(0.0, 0.0, 0.0)
	
	else: 
		if dot <= 0:
                	return Color(0.0, 0.0, 0.0)

 		else:
			return Color((dot * light.color.r * 
				      g[mindex][0].color.r * 
		                      g[mindex][0].finish.diffuse) + SS.r,
                             	     (dot * light.color.g * 
				      g[mindex][0].color.g * 
				      g[mindex][0].finish.diffuse) + SS.g,
                             	     (dot * light.color.b * 
				      g[mindex][0].color.b * 
				      g[mindex][0].finish.diffuse) + SS.b)
	


def color_finder(g, sphere_list, ray, color, light):
	mindex = 0
        for i in range(1, len(g)):
		if (length_vector(vector_from_to(ray.pt, g[mindex][1])) > 
	            length_vector(vector_from_to(ray.pt, g[i][1]))):
			mindex = i
	d = diffuse_finder(g, sphere_list, ray, color, light, mindex)
	return Color((g[mindex][0].color.r  * 
		      g[mindex][0].finish.ambient * color.r) + d.r,
                     (g[mindex][0].color.g  * 
		      g[mindex][0].finish.ambient * color.g) + d.g,
                     (g[mindex][0].color.b  * 
		      g[mindex][0].finish.ambient * color.b) + d.b)

def cast_ray(ray, sphere_list, color, light):
	
	g = find_intersection_points(sphere_list, ray)
	if g == []:
		return Color(1.0, 1.0, 1.0)
        else:	
		return color_finder(g, sphere_list, ray, color, light)
		
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
        y_interval = (max_y - min_y) / float(height)
        x_interval = (max_x - min_x) / float(width)
        print 'P3'
        print width, height
        print 255
        for j in range(0, height):
                for i in range(0, width):
                        x = min_x + x_interval * i
                        y = max_y - y_interval * j
                        z = 0
                        point = Point(x, y, z)
                        vector1 = vector_from_to(eye_point, point)
                        RRay = Ray(eye_point, vector1)
                        c = cast_ray(RRay, sphere_list, color, light)
			answer = scale_color(c, 255) 
			print int(answer.r), int(answer.g), int(answer.b)




