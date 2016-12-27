from data import *
from vector_math import *
from collisions import *


def cast_ray(ray, sphere_list, clr, lght, pt):
    #checks if ray intersects a sphere
    if find_intersection_points(sphere_list, ray) != []:
	nearest = 0
        for s in range(len(sphere_list)):
            #checks if there is more than one sphere
	    if len(find_intersection_points(sphere_list, ray)) > 1:
	        if dist_from_ray_pt(ray, sphere_list[s]) <= \
	           dist_from_ray_pt(ray, sphere_list[nearest]):
		    nearest = s

        int_pt = sphere_intersection_point(ray, sphere_list[nearest])
        p_sub_e = point_off_sphere(sphere_list[nearest], int_pt)
	sp_norm = sphere_normal_at_point(sphere_list[nearest], int_pt)
        norm_to_light = normalize_vector(vector_from_to(p_sub_e, lght.pt))
	dot_prod = dot_vector(sp_norm, norm_to_light)
	if dot_prod <= 0:
	    dot_prod = 0
	reflect_vec = difference_vector(norm_to_light, 
			                scale_vector(sp_norm, (2 * dot_prod)))
	view_dir = normalize_vector(vector_from_to(pt, p_sub_e))
	spec_intensity = dot_vector(reflect_vec, view_dir)
	if spec_intensity <= 0:
	    spec_intensity = 0
	spclr = sphere_list[nearest].finish.specular *\
	        (spec_intensity ** (1.0/sphere_list[nearest].finish.roughness))

        #checks if distance between pt off sphere and light pt is
        #greater than pt off sphere and any obstructing sphere
	diff = sphere_list[nearest].finish.diffuse
	ray_to_light = Ray(p_sub_e, vector_from_to(p_sub_e, lght.pt))
	for s in range(len(sphere_list)):
            if sphere_intersection_point(ray_to_light, sphere_list[s]):
	        if length_vector(vector_from_to(p_sub_e,
                   sphere_intersection_point(ray_to_light, sphere_list[s])))\
                   <= length_vector(ray_to_light.dir):
                    diff = 0

	r = sphere_list[nearest].color.r *\
	    sphere_list[nearest].finish.ambient * clr.r +\
            (dot_prod * lght.color.r * sphere_list[nearest].color.r * diff) +\
            (lght.color.r * spclr)
	if r > 1.0:
	    r = 1.0
	g = sphere_list[nearest].color.g *\
	    sphere_list[nearest].finish.ambient * clr.g +\
            (dot_prod * lght.color.g * sphere_list[nearest].color.g * diff) +\
            (lght.color.g * spclr)
	if g > 1.0:
            g = 1.0
	b = sphere_list[nearest].color.b *\
	    sphere_list[nearest].finish.ambient * clr.b +\
            (dot_prod * lght.color.b * sphere_list[nearest].color.b * diff) +\
            (lght.color.b * spclr)
	if b > 1.0:
	    b = 1.0

	return Color(r, g, b)

    else:
	return Color(1.0, 1.0, 1.0) #returns white


def dist_from_ray_pt(ray, sphere):
    return length_vector(difference_point(ray.pt, 
	                                  sphere_intersection_point(ray, 
						                    sphere)))


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
		  sphere_list, clr, lght):
    dy = (max_x - min_x) / float(width)
    dx = (max_y - min_y) / float(height)
    y = max_y
    x = min_x
    while y > min_y:
        while x < max_x:
	    color = cast_ray(Ray(eye_point, 
		                 vector_from_to(eye_point, Point(x, y, 0))),
			     sphere_list, clr, lght, eye_point)
            print int(color.r * 255), int(color.g * 255), int(color.b * 255)

	    x += dx
        y -= dy
	x = min_x


def point_off_sphere(sphere, point): #refered to as 'p sub e'
    return translate_point(point, scale_normal(sphere, point))


def scale_normal(sphere, point):
    return scale_vector(sphere_normal_at_point(sphere, point), 0.01)

