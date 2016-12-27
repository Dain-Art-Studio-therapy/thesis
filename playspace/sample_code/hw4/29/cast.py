# Han Tran | CPE101-01,02 | Assignment 4-Part4 | Professor: Aaron Keen
import math
import data
import utility
import vector_math
import collisions

# ----- Supportive Functions ----- #
	#Find and return the nearest point to the origin 
def distance_calculation(pt1, pt2):
	return math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2 + (pt1.z - pt2.z)**2)

	
	#Find the smallest value in list and return its index
def index_of_smallest(lst):
	mindex = 0
	for i in range(len(lst)):
		if lst[i] < lst[mindex]:
			mindex = i
	return mindex

	
	#Find point nearest to the origin
def nearest_origin(lst, ori):
	dis = []
	for i in range(len(lst)):
		dis.append(distance_calculation(lst[i][1], ori))
	return index_of_smallest(dis)


   # Find color ambient for cast_ray
def color_ambient(color1, color2, scalar):
   return data.Color(color1.r * color2.r * scalar, color1.g * color2.g *scalar, color1.b * color2.b *scalar)


	# Find color diffuse with light for cast_ray
def color_finish(color1, color2, scalar1, scalar2):
    return data.Color(color1.r * color2.r * scalar1 * scalar2, color1.g * color2.g * scalar1 * scalar2, color1.b * color2.b * scalar1 * scalar2)


	# Calculate p_epsilon
def p_epsilon(sp_intersect, scale):
   sp_normVector = collisions.sphere_normal_at_point(sp_intersect[0], sp_intersect[1])
   sp_normScale = vector_math.scale_vector(sp_normVector, scale)
   return data.Point(sp_intersect[1].x + sp_normScale.x, sp_intersect[1].y + sp_normScale.y, sp_intersect[1].z + sp_normScale.z)


   # Calculate the distance between the colliding sphere and pe, light source -> find the angle from between light's point and sphere normal (i.e N and Ldir)
def find_light_diffuse(sphere_pts, pt1, pt2, N, Ldir):
   for sphere in sphere_pts:
      d = distance_calculation(sphere[1], pt1)
      D = distance_calculation(pt1, pt2)
      if d < D:
         return 0.0
   return vector_math.dot_vector(N, Ldir)


# ----- MAIN FUNCTIONS ----- #
# cast_ray
def cast_ray(ray, sphere_list, Color, Light, Point):
   intersect_pts = collisions.find_intersection_points(sphere_list, ray)
   light_angle = 180
   if intersect_pts == []:
      return data.Color(1.0, 1.0, 1.0)
   else:
      index_near = nearest_origin(intersect_pts, ray.pt)
      sp_color = intersect_pts[index_near][0].color
      sp_finish = intersect_pts[index_near][0].finish.ambient
      color_amb = color_ambient(sp_color, Color, sp_finish)
      pe = p_epsilon(intersect_pts[index_near], 0.01)
      N = collisions.sphere_normal_at_point(intersect_pts[index_near][0], intersect_pts[index_near][1])
      Ldir = vector_math.normalize_vector(vector_math.vector_from_to(pe, Light.pt))
      visible = vector_math.dot_vector(N, Ldir)
      if visible > 0:
         ray_pe_Ldir = data.Ray(pe, Ldir)
         check_collide = collisions.find_intersection_points(sphere_list, ray_pe_Ldir)
         if check_collide == []:
            color_diffuse = color_finish(Light.color, sp_color, intersect_pts[index_near][0].finish.diffuse, visible)
         else:
            light_angle = find_light_diffuse(check_collide, pe, Light.pt, N, Ldir)
            color_diffuse = color_finish(Light.color, sp_color, intersect_pts[index_near][0].finish.diffuse, light_angle)
      else:
         color_diffuse = data.Color(0, 0, 0)
      #color_diffuse = data.Color(color_amb.r + color_diffuse.r, color_amb.g + color_diffuse.g, color_amb.b + color_diffuse.b)
   # Specular calculation
      LdotN = vector_math.dot_vector(Ldir, N)
      Nscl = vector_math.scale_vector(N , 2*LdotN)
      reflection = minus_vec(Ldir, Nscl)
      Vdir = vector_math.normalize_vector(vector_math.vector_from_to(Point, pe))
      specular_inten = vector_math.dot_vector(reflection, Vdir)
      if specular_inten > 0:
         sp_specular = intersect_pts[index_near][0].finish.specular
         sp_roughness = intersect_pts[index_near][0].finish.roughness
         powerSpec = specular_inten**(1/sp_roughness)
         specular = data.Color(Light.color.r * sp_specular * powerSpec, Light.color.g * sp_specular * powerSpec, Light.color.b * sp_specular * powerSpec)
      else:
         specular = data.Color(0, 0, 0)
   return data.Color(color_amb.r + color_diffuse.r + specular.r, color_amb.g + color_diffuse.g + specular.g, color_amb.b + color_diffuse.b + specular.b)


def minus_vec(vec1, vec2):
   return data.Vector(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)


# cast_all_ray
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, Color, Light):
   del_x = (max_x - min_x)/float(width)
   del_y = (max_y - min_y)/float(height)
   z = 0
	# Find the ray from eye_point to each pixel on the rectangle
   for i in range(height): # enter each row
      y = max_y - i*del_y
      for j in range(width):  # enter each column
         x = min_x + j*del_x
         pixel_pt = data.Point(x, y, z)
         vec_eye_pixel = vector_math.difference_point(pixel_pt, eye_point)
         ray = data.Ray(eye_point, vec_eye_pixel)
			# check if the ray hits spheres
         color = cast_ray(ray, sphere_list, Color, Light, eye_point)
         r = no_excess(color.r)
         g = no_excess(color.g)
         b = no_excess(color.b)
         R = int(r*255)
         G = int(g*255)
         B = int(b*255)
         #R = int(color.r*255)
         #G = int(color.g*255)
         #B = int(color.b*255)
         print R, G, B


def no_excess(c):
   if int(c) > 1.0:
      return 1.0
   else:
      return c


def print_header(width, height):
   print 'P3'
   print(str(width) + ' ' + str(height))
   print 255
