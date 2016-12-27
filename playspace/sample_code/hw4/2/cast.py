import collisions
import data
import vector_math

def cast_ray(ray, sphere_list, color, light, Point):
   n = collisions.find_intersection_points(sphere_list, ray)
   if (n == []):
      return data.Color(255, 255, 255)
   sphere = n[0][0]
   start = n[0][1]
   for e in n:
      if (distance(start, ray.pt) > distance(e[1], ray.pt)):
         sphere = e[0]
         start = e[1]
   sphere_norm = collisions.sphere_normal_at_point(sphere, start)
   scaled_norm = vector_math.scale_vector(sphere_norm, 0.01)
   off_pt = vector_math.translate_point(start, scaled_norm)
   vec_light = vector_math.vector_from_to(off_pt, light.pt)
   norm_light = vector_math.normalize_vector(vec_light)
   dot = vector_math.dot_vector(sphere_norm, norm_light)
   refpt1 = multiply(sphere_norm, (2 * dot))
   ref = vec_subt(norm_light, refpt1)
   vec_eye = vector_math.vector_from_to(Point, off_pt)
   norm_eye = vector_math.normalize_vector(vec_eye)
   intensity = vector_math.dot_vector(ref, norm_eye)
   if (dot > 0):
      rayz = data.Ray(off_pt, norm_light)
      new = collisions.find_intersection_points(sphere_list, rayz)
      for e in new:
         if (distance(e[1], off_pt) < distance(light.pt, off_pt) and e[0] != sphere):
            r = sphere.color.r * color.r * sphere.finish.ambient
            gr = sphere.color.g * color.g * sphere.finish.ambient
            b = sphere.color.b * color.b * sphere.finish.ambient
            return data.Color(r, gr, b)
      if (intensity > 0):
         r = sphere.color.r * color.r * sphere.finish.ambient + sphere.color.r * light.color.r * dot * sphere.finish.diffuse + light.color.r * sphere.finish.specular * intensity ** (1 / sphere.finish.roughness)  
         gr = sphere.color.g * color.g * sphere.finish.ambient + sphere.color.g * light.color.g * dot * sphere.finish.diffuse + light.color.g * sphere.finish.specular * intensity ** (1 / sphere.finish.roughness)
         b = sphere.color.b * color.b * sphere.finish.ambient + sphere.color.b * light.color.b * dot * sphere.finish.diffuse + light.color.b * sphere.finish.specular * intensity ** (1 / sphere.finish.roughness)
         return data.Color(r, gr, b)

      r = sphere.color.r * color.r * sphere.finish.ambient + sphere.color.r * light.color.r * dot * sphere.finish.diffuse
      gr = sphere.color.g * color.g * sphere.finish.ambient + sphere.color.g * light.color.g * dot * sphere.finish.diffuse
      b = sphere.color.b * color.b * sphere.finish.ambient + sphere.color.b * light.color.b * dot * sphere.finish.diffuse
      return data.Color(r, gr, b)

   r = sphere.color.r * color.r * sphere.finish.ambient
   gr = sphere.color.g * color.g * sphere.finish.ambient
   b = sphere.color.b * color.b * sphere.finish.ambient
   return data.Color(r, gr, b)
   
def distance(point, point1):
   vec = vector_math.difference_point(point, point1)
   dist = vector_math.length_vector(vec)
   return dist


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,sphere_list, color, light):
   pixel_col_inc = (max_x - min_x) /float(width)
   pixel_row_inc = (max_y - min_y) /float(height)
   for h in range(0, height):
      for w in range(0, width):
         x = (min_x + w * pixel_col_inc)
         y = (max_y - h * pixel_row_inc)
         pt = data.Point(x, y, 0)
         vec = vector_math.vector_from_to(eye_point, pt)
         ray = data.Ray(eye_point, vec)
         cst = cast_ray(ray, sphere_list, color, light, eye_point)  
         print (cst.r)
         print int(cst.g)
         print int(cst.b)

def multiply(vector, v):
   x = vector.x * v
   y = vector.y * v
   z = vector.z * v
   return data.Vector(x, y, z)
 
def vec_subt(vector, vector2):
   x = vector.x - vector2.x
   y = vector.y - vector2.y
   z = vector.z - vector2.z
   return data.Vector(x, y, z)
