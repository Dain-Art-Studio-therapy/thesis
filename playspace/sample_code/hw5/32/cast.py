from collisions import *
from data import *
from vector_math import *
from math import *


def cast_ray(ray, sphere_list, amb_color, light, eye_pt):
   # find intersetction points (sphere, point)
   sect_pts = find_intersection_points(sphere_list, ray)
   
   # return white if no matches
   if sect_pts == []:
      return Color(1.0, 1.0, 1.0)

   # Get values for return color
   sect = find_closest_intersection_vals(sect_pts, ray)
   sphere = sect[0]
   pt = sect[1]
   
   # Get light info for diffuse
   l_info = light_info(sphere, pt, light, sphere_list)
   e_pt = l_info[0]
   visible_dot = l_info[1]
   l_dir = l_info[2]
   n_vec = l_info[3]
   light_cont = l_info[4]

   # Get specular info
   r_vec = difference_vector(l_dir, scale_vector(n_vec, 2 * visible_dot))
   v_dir = normalize_vector(vector_from_to(eye_pt, e_pt))
   spec_intense = dot_vector(r_vec, v_dir)

   # Get handle on sphere info
   s_color = sphere.color
   s_finish = sphere.finish
   s_f_ambient = s_finish.ambient
   s_f_roughness = s_finish.roughness
   s_f_specular = s_finish.specular
   
   # Determine whether spec needs to be added
   spec_color = Color(0.0, 0.0, 0.0)
   if spec_intense > 0 and light_cont == True:
      spec_rough_val = spec_intense ** (1.0 / s_f_roughness)
      spec_color = scale_color(light.color, [s_f_specular, spec_rough_val])


   # Calculate diffuse if necessary
   diffuse_color = Color(0.0, 0.0, 0.0)
   if light_cont == True:
      diffuse_color = mult_colors(light.color, s_color)
      diffuse_color = scale_color(diffuse_color, [visible_dot, s_finish.diffuse])

   # Calculate color vals
   n_color = mult_colors(s_color, amb_color)
   n_color = scale_color(n_color, [s_f_ambient])
   n_color = combine_colors([n_color, diffuse_color, spec_color])

   return n_color

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light, file):
   # Calculate differences
   x_diff = (float(max_x) - float(min_x)) / width
   y_diff = (float(max_y) - float(min_y)) / height

   # Run for loops to iterate through
   for y in range(int(height)):
      for x in range(int(width)):
         y_coord = max_y - (y * y_diff)
         x_coord = min_x + (x * x_diff)
         pt = Point(x_coord, y_coord, 0)
         vec = difference_point(pt, eye_point)
         ray = Ray(eye_point, vec)
         
         # Get color
         color = cast_ray(ray, sphere_list, amb_color, light, eye_point)
         con_color = color_255(color)

         file.write('{0} {1} {2}\n'.format(con_color.r, con_color.g, con_color.b))
# Color stuff ********************************************************

def combine_colors(colors):
   c = Color(0, 0, 0)
   for col in colors:
      c.r += col.r
      c.g += col.g
      c.b += col.b
   
   return c

def scale_color(c, vals):
   # First calc product of vals
   scale_factor = 1
   for e in vals:
      scale_factor *= e

   # Return scaled color
   return Color(c.r * scale_factor, c.g * scale_factor, c.b * scale_factor)

def mult_colors(c1, c2):
   return Color(c1.r * c2.r, c1.g * c2.g, c1.b * c2.b)

def color_255(color):
   return Color(min(int(color.r * 255), 255),
                min(int(color.g * 255), 255),
                min(int(color.b * 255), 255))


# Cast ray functions ****************************************************

# Return (e_pt, visible_dot, l_dir, n_vec diffuse_cont)
def light_info(sphere, pt, light, sphere_list):

   # Calcs normal vector, scales vector by factor, and translates point by vector
   scale_factor = 0.01
   n_vec = sphere_normal_at_point(sphere, pt)
   scaled_vec = scale_vector(n_vec, scale_factor)
   
   e_pt = translate_point(pt, scaled_vec)
   
   l_dir = normalize_vector(vector_from_to(e_pt, light.pt))
   
   # Calculate dot product and find out if light is visible
   visible_dot = dot_vector(n_vec, l_dir)
   diffuse_cont = True

   if visible_dot > 0:
      
      # Check if a sphere is in between the light source and e_pt
      light_vector = vector_from_to(e_pt, light.pt)
      light_ray = Ray(e_pt, light_vector)
      light_sect_pts = find_intersection_points(sphere_list, light_ray)

      # Test any intersection points against the light_dist
      light_dist = length_vector(light_vector)
      for l_sect in light_sect_pts:
         # Calculate all distances and test against
         dist = distance_between_points(l_sect[1], e_pt)
         if dist < light_dist:
            diffuse_cont = False
            break
        
   # If the dot product is 0, don't contribute
   else:
      diffuse_cont = False

   return (e_pt, visible_dot, l_dir, n_vec, diffuse_cont)


def find_closest_intersection_vals(sect_pts, ray):
   # determine which intersection point is closest
   # update these two vars as we loop through
   closest_index = 0
   current_length = length_vector(difference_point(ray.pt, sect_pts[0][1]))
   for i in range(1, len(sect_pts)):
      length = length_vector(difference_point(ray.pt, sect_pts[i][1]))
      if length < current_length:
         closest_index = i

   return sect_pts[closest_index]

def distance_between_points(pt1, pt2):
   return sqrt((pt2.x-pt1.x) ** 2 + (pt2.y-pt1.y) ** 2 + (pt2.z-pt1.z) ** 2)
