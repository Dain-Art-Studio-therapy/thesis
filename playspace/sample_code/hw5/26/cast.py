import collisions
from collisions import sphere_normal_at_point

import vector_math
from vector_math import distance
from vector_math import translate_point
from vector_math import scale_vector
from vector_math import normalize_vector
from vector_math import dot_vector
from vector_math import vector_from_to
from vector_math import difference_vector

import data
import utility 


def cast_all_rays(min_x, max_x, min_y, max_y, width, height,\
   eye_point, sphere_list, color, light):
   pixel_color = []
   dx = (max_x - min_x)/float(width)
   dy = (max_y - min_y)/float(height)
   for j in range(height): 
      for i in range(width):
         ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point,\
            data.Point(min_x + i*dx, max_y - j*dy, 0)))
         closest_sphere_color = cast_ray(ray, sphere_list, color, light, \
            eye_point)
         pixel_color.append([min(int(closest_sphere_color.r*255), 255), \
            min(int(closest_sphere_color.g*255), 255),\
            min(int(closest_sphere_color.b*255), 255)])
   return pixel_color


def cast_ray(ray, sphere_list, color, light, point):
   closest_sphere = find_closest_sphere(ray, sphere_list)
   
   if closest_sphere is not None:

      intersected_sphere = closest_sphere[0]
      intersected_pt = closest_sphere[1]
      normalized_vector = sphere_normal_at_point(intersected_sphere,\
         intersected_pt)
      translating_vector = scale_vector(normalized_vector, 0.01)

      new_point = translate_point(intersected_pt, translating_vector)
      L_dir = normalize_vector(vector_from_to(new_point, light.pt))
      dot_product = dot_vector(normalized_vector, L_dir) 

      ray_to_light = data.Ray(new_point, L_dir)

      reflection_vector = difference_vector(L_dir, \
         scale_vector(normalized_vector, dot_product*2))
      V_dir = normalize_vector(vector_from_to(point, new_point))

      spec_intensity = dot_vector(reflection_vector, V_dir)

      # Diffuse Effects (shadowing)
      if dot_product <= 0 or\
      no_light_cast(ray_to_light, sphere_list):
         diffuse_effect = data.Color(0.0, 0.0, 0.0)
      else:
         diffuse_effect = data.Color(\
            dot_product*light.color.r*intersected_sphere.color.r*\
            intersected_sphere.finish.diffuse,\
            dot_product*light.color.g*intersected_sphere.color.g*\
            intersected_sphere.finish.diffuse, \
            dot_product*light.color.b*intersected_sphere.color.b*\
            intersected_sphere.finish.diffuse)
      
      # Specular Value of Finish (extra shine :))
      if spec_intensity <= 0 or\
      no_light_cast(ray_to_light, sphere_list):
         spec_val = data.Color(0, 0, 0)
      else:
         spec_val = data.Color(\
            light.color.r*intersected_sphere.finish.specular*\
            spec_intensity**(1/intersected_sphere.finish.roughness),\

            light.color.g*intersected_sphere.finish.specular*\
            spec_intensity**(1/intersected_sphere.finish.roughness),\

            light.color.b*intersected_sphere.finish.specular*\
            spec_intensity**(1/intersected_sphere.finish.roughness))


      R = intersected_sphere.color.r*color.r*intersected_sphere.finish.ambient\
         + diffuse_effect.r + spec_val.r
      G = intersected_sphere.color.g*color.g*intersected_sphere.finish.ambient\
         + diffuse_effect.g + spec_val.g
      B = intersected_sphere.color.b*color.b*intersected_sphere.finish.ambient\
         + diffuse_effect.b + spec_val.b
   
      return data.Color(R, G, B)  
   else:
      return data.Color(1.0, 1.0, 1.0)


# CAST.PY HELPER FUNCTIONS   
def find_closest_sphere(ray, sphere_list):
   intersect_list = collisions.find_intersection_points(sphere_list, ray) 
   if intersect_list != []: 
      closest_sphere = intersect_list[0]   
      for i in range(len(intersect_list)):
         if distance(ray.pt, intersect_list[i][1]) <\
            distance(ray.pt, closest_sphere[1]):

            closest_sphere = intersect_list[i]
      return closest_sphere
   else:
      return None

def no_light_cast(light_ray, sphere_list):
   lit_sphere = find_closest_sphere(light_ray, sphere_list)
   return lit_sphere is not None
     


## PART 1 cast.py and casting_test.py functions
# intersection_pts.append((s, sphere_intersection_point(ray, s))
def cast_ray_1(ray, sphere_list):
   return_list = collisions.find_intersection_points(sphere_list, ray)    
   return return_list != [] 

def cast_all_rays_1(min_x, max_x, min_y, max_y, width, height, eye_point, \
   sphere_list):
   dx = (max_x - min_x)/float(width)
   dy = (max_y - min_y)/float(height)
   for j in range(height): 
      for i in range(width):
         ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, \
            data.Point(min_x + i*dx, max_y - j*dy, 0)))
         if cast_ray_1(ray, sphere_list) is True:
            print '0 0 0'
         else:
            print '255 255 255'
            

  
