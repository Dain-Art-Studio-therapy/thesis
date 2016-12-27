import collisions 
from vector_math import *
from data import *
def cast_ray(ray, sphere_list):
	collisions.find_intersection_points(ray, sphere_list)
	if sphere_list is not []:
		if collisions.find_intersection_points(ray, sphere_list) is not None:
			return True
		else:
			return False
	else:
		return False

def number_pts_hit(ray, sphere_list):
	found_pts = collisions.find_intersection_points(ray, sphere_list)
	return len (found_pts)

def first_sphere_hit(eye_point, ray, sphere_list):
	found_pts = collisions.find_intersection_points(ray, sphere_list)
	temporary_list = []
	for sp_pt_tuple in found_pts:
		distance_vect= difference_point(sp_pt_tuple[1], ray.pt)
		square_vect_leng = square_length_vector(distance_vect) 
		Tuple_to_be_sorted = (square_vect_leng, sp_pt_tuple[0])
		temporary_list.append(Tuple_to_be_sorted)
		temporary_list.sort()
		first_tuple = temporary_list[0]
	return first_tuple[1]

def first_pt_hit(eye_point, ray, sphere_list):
	found_pts = collisions.find_intersection_points(ray, sphere_list)
	temporary_list = []
	for sp_pt_tuple in found_pts:
		distance_vect = difference_point(sp_pt_tuple[1], ray.pt)
		square_vect_leng = square_length_vector(distance_vect) 
		Tuple_to_be_sorted = (square_vect_leng, sp_pt_tuple[1])
		temporary_list.append(Tuple_to_be_sorted)
		temporary_list.sort()
		first_tuple = temporary_list[0]
	return first_tuple[1]

def reject_pts(eye_point, ray, sphere_list):
	found_pts = collisions.find_intersection_points(ray, sphere_list)
	fph=first_pt_hit(eye_point, ray, sphere_list)
	rejected_points = []
	for point in found_pts:
		if point != fph:
			rejected_points.append(point)
	return rejected_points

def point_pe(eye_point, ray, sphere_list):
	first_point_hit = first_pt_hit(eye_point, ray, sphere_list)
	first_sp_hit = first_sphere_hit(eye_point, ray, sphere_list)
#	norm = normalize_vector(ray.dir)
	to_be_normed = difference_point(first_point_hit, first_sp_hit.center)
	norm = normalize_vector(to_be_normed)
	scaled_vect = scale_vector(norm, .01)
	pe = translate_point(first_point_hit, scaled_vect)
	return pe
def there_is_a_middle_sphere():
#	found_pts = collisions.find_intersection_points(ray, sphere_list)
#	if len (found_pts)>1:
#		fph=first_pt_hit(eye_point, ray, sphere_list)
#		if fph != :
#			return True
#		else:
#			return False
#
#	else:
		return False

def diffuse_contribution (eye_point, ray, sphere_list, light): #add in sphere? # take out pe stuff   
	light_color = light.color
	first_sp_hit = first_sphere_hit(eye_point, ray, sphere_list)
	pe = point_pe(eye_point, ray, sphere_list)
	pe_to_light = difference_point(light.point, pe)
	to_be_normed = difference_point(pe, first_sp_hit.center)
	norm = normalize_vector(to_be_normed)

	if there_is_a_middle_sphere() is False:
		diffuse_contrib = Color (light_color.r * first_sp_hit.color.r 
			* first_sp_hit.finish.diffuse,
			light_color.g * first_sp_hit.color.g
			* first_sp_hit.finish.diffuse,
			light_color.b * first_sp_hit.color.b 
			* first_sp_hit.finish.diffuse)
	if there_is_a_middle_sphere() is True:
		diffuse_contrib = Color (0.0, 0.0 , 0.0)
	return diffuse_contrib 

def pe_color_factor(eye_point, ray, sphere_list, light):# ref dc in this
	pe = point_pe(eye_point, ray, sphere_list)
	first_sp_hit = first_sphere_hit(eye_point, ray, sphere_list)
	to_be_normed = difference_point(pe, first_sp_hit.center)
	norm = normalize_vector(to_be_normed)#want center of fsphere to pe normified
	light_pt = light.point
	dif_pt= difference_point(light_pt, pe)
	pe_to_light = normalize_vector(dif_pt)
	norm_doted_w_plight = dot_vector(norm, pe_to_light)
	dc = diffuse_contribution (eye_point, ray, sphere_list, light)
	if norm_doted_w_plight>0:

		diffuse_color= Color (dc.r * norm_doted_w_plight, 
			dc.g * norm_doted_w_plight,
			dc.b * norm_doted_w_plight)
		return diffuse_color

	else:
		return Color (0.0,0.0,0.0)



def color_calculation_ambient(eye_point, ray, sphere_list, ambient_light):
	found_pts = collisions.find_intersection_points(ray, sphere_list)
	first_sp_hit = first_sphere_hit(eye_point, ray, sphere_list)
	rjpts = reject_pts(eye_point, ray, sphere_list)  
	sphere_color = first_sp_hit.color
	new_red = sphere_color.r * first_sp_hit.finish.ambient * ambient_light.r
	new_green = sphere_color.g * first_sp_hit.finish.ambient * ambient_light.g
	new_blue = sphere_color.b * first_sp_hit.finish.ambient * ambient_light.b
	new_color = Color (new_red, new_green, new_blue)
	return new_color

def specular_component(eye_point, ray, sphere_list,light):
	pe = point_pe(eye_point, ray, sphere_list)
	light_pt = light.point
	dif_pt= difference_point(light_pt, pe) #ldir
	pe_to_light = normalize_vector(dif_pt)
	first_sp_hit = first_sphere_hit(eye_point, ray, sphere_list)
	to_be_normed = difference_point(pe, first_sp_hit.center)
	norm = normalize_vector(to_be_normed)#N
	double_dif_pt_dot_norm = 2*(dot_vector(dif_pt,to_be_normed))#was norm
	subtracted_vector = scale_vector(norm, double_dif_pt_dot_norm) #was norm
	reflection_vector = difference_vector(dif_pt, subtracted_vector)#?


	from_eye_to_pe = difference_point(pe, eye_point)
	norm_eye_p = normalize_vector(from_eye_to_pe) #vdir
	specular_intensity =dot_vector(reflection_vector,norm_eye_p)
	if specular_intensity>0:
		spec_r = (light.color.r*first_sp_hit.finish.specular*specular_intensity
			**(1/float(first_sp_hit.finish.roughness)))
		spec_g = (light.color.r*first_sp_hit.finish.specular*specular_intensity
			** (1/float(first_sp_hit.finish.roughness)))
		spec_b = (light.color.r*first_sp_hit.finish.specular*specular_intensity
			** (1/float(first_sp_hit.finish.roughness)))
		spec_component = Color (spec_r,spec_g,spec_b)
#	else:
		spec_component = Color (0.0,0.0,0.0)
		return spec_component


def total_color(ambient_light, eye_point, ray, sphere_list, light):
#	spec = specular_component
	diffuse_color = pe_color_factor(eye_point, ray, sphere_list, light)
#	spec_component = specular_component(eye_point, ray, sphere_list,light)
	spec_component = specular_component(eye_point, ray, sphere_list,light)
	new_color = color_calculation_ambient(eye_point, ray, sphere_list, 
		ambient_light)
	total_color = Color (diffuse_color.r + new_color.r,
	diffuse_color.g + new_color.g,
	diffuse_color.b + new_color.b)
	return total_color




def color_to_be_cast(ambient_light, eye_point, ray, sphere_list, light):
	nph = number_pts_hit(ray, sphere_list)
	for i in range(nph):
		if i==0:
			color = total_color(ambient_light, eye_point, ray, sphere_list, 
				light)
		if i>=1:
		 	color = (0.0, 0.0, 0.0)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
	eye_point, sphere_list, ambient_light, light):
		top_left = Point (min_x, max_y, 0)
		bottom_right = Point (max_x, min_y, 0)
		dx=(max_x-min_x)/float(width)
		dy=(max_y-min_y)/float(height)
		
		y_counter=max_y
		print "P3"
		print "1024 768"
		print "255"
#		rj_pts = reject_pts(eye_point, ray, sphere_list)
		while y_counter <= max_y and y_counter>min_y:
			x_counter=min_x
			while x_counter >= min_x and x_counter<max_x:
				to_point =  Point (x_counter,y_counter,0)
				ray = Ray (eye_point,(difference_point(to_point, eye_point)),
					ambient_light)
				ray_casting = cast_ray(ray, sphere_list)
				if cast_ray(ray, sphere_list) is True:
					color = total_color(ambient_light, eye_point, 
						ray, sphere_list, light)
					print color
				else:
					print Color (1.0, 1.0, 1.0)
				x_counter+=dx
			y_counter -= dy

	#if double>1.0 max= 255
