import collisions
import data
import vector_math
import math

def cast_ray(ray, sphere_list, ambient_color, point_light, eye_pos):
   intersections = collisions.find_intersection_points(sphere_list, ray)
   if len(intersections) > 0:
      nearest = nearest_eye_point(ray, sphere_list)[0]

      # calculating pE
      intersection_point = collisions.sphere_intersection_point(ray, nearest)
      v1 = collisions.sphere_normal_at_point(nearest, intersection_point)
      scaled_v1 = vector_math.scale_vector(v1, 0.01)
      p_E = vector_math.translate_point(intersection_point, scaled_v1)

      light_dir = vector_math.normalize_vector(vector_math.
                                     difference_point(point_light.pt, p_E))
      visible_light = vector_math.dot_vector(v1, light_dir)
      ray1 = data.Ray(p_E, light_dir)
      sp_in_path = collisions.find_intersection_points(sphere_list, ray1)

      reflection_v = vector_math.difference_vector(light_dir,
                     vector_math.scale_vector(v1, 2 * visible_light))
      v_dir = vector_math.normalize_vector(
              vector_math.vector_from_to(eye_pos, p_E))
      spec_intensity = vector_math.dot_vector(reflection_v, v_dir)
      
      if visible_light > 0 and sp_in_path == []:
         if spec_intensity > 0:
            return data.Color(nearest.color.r * (ambient_color.r *
                 nearest.finish.ambient +
                 nearest.finish.diffuse * 
                 point_light.color.r * visible_light)+(
                 point_light.color.r * 
                 nearest.finish.specular *
                 spec_intensity ** (1/nearest.finish.roughness)),
                nearest.color.g * (ambient_color.g *
                 nearest.finish.ambient +
                 nearest.finish.diffuse * 
                 point_light.color.g * visible_light)+(
                 point_light.color.g * 
                 nearest.finish.specular *
                 spec_intensity ** (1/nearest.finish.roughness)),
                nearest.color.b * (ambient_color.b *
                 nearest.finish.ambient +
                 nearest.finish.diffuse * 
                 point_light.color.b * visible_light)+(
                 point_light.color.b * 
                 nearest.finish.specular *
                 spec_intensity ** (1/nearest.finish.roughness)))
         else:
            return data.Color(nearest.color.r * (ambient_color.r *
                 nearest.finish.ambient +
                 nearest.finish.diffuse * 
                 point_light.color.r * visible_light),
                nearest.color.g * (ambient_color.g *
                 nearest.finish.ambient +
                 nearest.finish.diffuse * 
                 point_light.color.g * visible_light),
                nearest.color.b * (ambient_color.b *
                 nearest.finish.ambient +
                 nearest.finish.diffuse * 
                 point_light.color.b * visible_light))

      else:
         if spec_intensity > 0:
            return data.Color(nearest.color.r * ambient_color.r *
                 nearest.finish.ambient + (point_light.color.r * 
                 nearest.finish.specular *
                 spec_intensity ** (1/nearest.finish.roughness)),
                nearest.color.g * ambient_color.g *
                 nearest.finish.ambient + (point_light.color.g * 
                 nearest.finish.specular *
                 spec_intensity ** (1/nearest.finish.roughness)),
                nearest.color.b * ambient_color.b *
                 nearest.finish.ambient + (point_light.color.b * 
                 nearest.finish.specular *
                 spec_intensity ** (1/nearest.finish.roughness)))
         else:
            return data.Color(nearest.color.r * ambient_color.r *
                 nearest.finish.ambient, nearest.color.g * ambient_color.g *
                 nearest.finish.ambient, nearest.color.b * ambient_color.b *
                 nearest.finish.ambient)
 
   return data.Color(1.0, 1.0, 1.0)


def nearest_eye_point(ray, sphere_list):
   intersections = collisions.find_intersection_points(sphere_list, ray)
   closest_sphere = intersections[0]
   for i in range(1, len(intersections)):
      if vector_math.length_vector(vector_math.difference_point(
                  intersections[i][1], ray.pt)) < vector_math.length_vector(
                  vector_math.difference_point(closest_sphere[1], ray.pt)):
         closest_sphere = intersections[i]
   return closest_sphere

def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
                  eye_point, sphere_list, ambient_color, point_light):
            
   file_object = open('image.ppm', 'w')

   print >> file_object, 'P3'
   print >> file_object, width, height
   print >> file_object, 255

   delta_x = (max_x - min_x) / width
   delta_y = (max_y - min_y) / height
   
   def ray_intersect_pt(x, y):
      return data.Point(min_x + x * delta_x, max_y - y * delta_y, 0.0)

   for y in range(height):
      for x in range(width):
         ray_direction = data.Ray(eye_point, vector_math.vector_from_to(
                                  eye_point, ray_intersect_pt(x, y)))

         get_color = cast_ray(ray_direction, sphere_list,
                              ambient_color, point_light, eye_point)

         if get_color is not data.Color(1.0, 1.0, 1.0):
            print >> file_object, int(cap_value(get_color.r * 255)), \
                  int(cap_value(get_color.g * 255)), \
                  int(cap_value(get_color.b * 255))
         else:
            print >> file_object, (int(255), int(255), int(255))

def cap_value(c):
   cap = 255
   if c > cap:
      return cap
   else:
      return c
      
         
