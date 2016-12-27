import data
import vector_math
import collisions
import sys

#up to part 3 cast ray
def cast_ray(ray, sphere_list, light):
   if sphere_list == []:
      return data.Color(1.0, 1.0, 1.0)

   intersections = collisions.find_intersection_points(sphere_list, ray)

   if intersections != None:
      closest = intersections[0]
      for i in range(1, len(intersections)):
         if vector_math.length_vector(vector_math.vector_from_to(ray.pt, intersections[i][1])) < vector_math.length_vector(vector_math.vector_from_to(ray.pt, closest[1])):
            closest = intersections[i]
      finish = closest[0].finish.ambient
      return  data.Color(closest[0].color.r * finish * light.color.r, closest[0].color.g * finish * light.color.g, closest[0].color.b * finish * light.color.b)
   return data.Color(1.0, 1.0, 1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_light, light, outfile):
#   print 'P3'
#   print width, height
#   print '255'

   dx = (max_x - min_x) / float(width)
   dy = (max_y - min_y) / float(height)

   py = max_y
   for y in range(height):
      for x in range(width):
         px = min_x + x*dx
         vector = vector_math.vector_from_to(eye_point, data.Point(px, py, 0))
         ray = data.Ray(eye_point, vector)
         color = color_conversion(cast_ray_1(ray, sphere_list, ambient_light, light, eye_point))
         outfile.write(str(color.r) + '\n')
         outfile.write(str(color.g) + '\n')
         outfile.write(str(color.b) + '\n')
      py -= dy

def color_conversion(color):
   return data.Color(min(255, int(color.r * 255)), min(255, int(color.g * 255)), min(255, int(color.b * 255)))

#part 4 and part 5 (hopefully)
def cast_ray_1(ray, sphere_list, ambient_light, light, eye_point):
   if sphere_list == []:
      return data.Color(1.0, 1.0, 1.0)

   intersections = collisions.find_intersection_points(sphere_list, ray)

   if intersections != None:
      closest_eye = 0
      for i in range(1, len(intersections)):
         if vector_math.length_vector(vector_math.vector_from_to(eye_point, intersections[i][1])) <= vector_math.length_vector(vector_math.vector_from_to(eye_point, intersections[closest_eye][1])):
            closest_eye = i

      s1 = intersections[closest_eye][0]
      closest_eye_point = intersections[closest_eye][1]

      normal = collisions.sphere_normal_at_point(s1, closest_eye_point)
      scale_normal = vector_math.scale_vector(normal, .01)
      closest_pe = vector_math.translate_point(closest_eye_point, scale_normal)

      n = collisions.sphere_normal_at_point(s1, closest_eye_point)
      ldir0 = vector_math.vector_from_to(closest_pe, light.pt)
      ldir = vector_math.normalize_vector(ldir0)
      ray_ldir = data.Ray(closest_pe, ldir)
      ldotn = vector_math.dot_vector(n, ldir)

      ldotn2 = 2 * ldotn
      n2 = vector_math.scale_vector(n, ldotn2)
      reflection_vector = vector_math.difference_vector(ldir, n2)

      vdir0 = vector_math.vector_from_to(eye_point, closest_pe)
      vdir = vector_math.normalize_vector(vdir0)

      specular_intensity = vector_math.dot_vector(reflection_vector, vdir)

      specular_r = light.color.r * s1.finish.specular * specular_intensity ** (1.0 / s1.finish.roughness)
      specular_g = light.color.g * s1.finish.specular * specular_intensity ** (1.0 / s1.finish.roughness)
      specular_b = light.color.b * s1.finish.specular * specular_intensity ** (1.0 / s1.finish.roughness)

      if specular_intensity <= 0:
         specular_r = 0
         specular_g = 0
         specular_b = 0

      if ldotn > 0:
         light_intersections = collisions.find_intersection_points(sphere_list, ray_ldir)
         if light_intersections != None:
            ldir_length = vector_math.length_vector(ldir0)

            shortest = ldir_length
            shortest_sphere = s1
            for (s, p) in light_intersections:
               if vector_math.length_vector(vector_math.vector_from_to(p, closest_pe)) < ldir_length:
                  shortest = vector_math.length_vector(vector_math.vector_from_to(p, closest_pe))
                  shortest_sphere = p

            if shortest_sphere != s1:
                  r = s1.color.r * ambient_light.r * s1.finish.ambient
                  g = s1.color.g * ambient_light.g * s1.finish.ambient
                  b = s1.color.b * ambient_light.b * s1.finish.ambient
                  return data.Color(r, g, b)
#shadow created by red sphere onto blue sphere

            elif shortest_sphere == s1: 
               diffuse_r = ldotn * light.color.r * s1.color.r * s1.finish.diffuse
               diffuse_g = ldotn * light.color.g * s1.color.g * s1.finish.diffuse
               diffuse_b = ldotn * light.color.b * s1.color.b * s1.finish.diffuse
               r = (s1.color.r * ambient_light.r * s1.finish.ambient) + diffuse_r + specular_r
               g = (s1.color.g * ambient_light.g * s1.finish.ambient) + diffuse_g + specular_g
               b = (s1.color.b * ambient_light.b * s1.finish.ambient) + diffuse_b + specular_b
               return data.Color(r, g, b)

         else:
            diffuse_r = ldotn * light.color.r * s1.color.r * s1.finish.diffuse
            diffuse_g = ldotn * light.color.g * s1.color.g * s1.finish.diffuse
            diffuse_b = ldotn * light.color.b * s1.color.b * s1.finish.diffuse
            r = s1.color.r * ambient_light.r * s1.finish.ambient + diffuse_r + specular_r
            g = s1.color.g * ambient_light.g * s1.finish.ambient + diffuse_g + specular_g
            b = s1.color.b * ambient_light.b * s1.finish.ambient + diffuse_b + specular_b
            return data.Color(r, g, b)

      else:
         r = s1.color.r * ambient_light.r * s1.finish.ambient
         g = s1.color.g * ambient_light.g * s1.finish.ambient
         b = s1.color.b * ambient_light.b * s1.finish.ambient
         return data.Color(r, g, b)
#light doesn't hit this part of the sphere
 
   return data.Color(1.0, 1.0, 1.0)
