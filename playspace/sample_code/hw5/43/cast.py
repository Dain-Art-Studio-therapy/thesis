import data 
import collisions 
import vector_math
import math

def color_finish(col,fin):
   return data.Color((col.r * fin),(col.g * fin),(col.b * fin))


def color_mult(c1,c2):
   return data.Color((c1.r * c2.r),(c1.g * c2.g),(c1.b * c2.b))


def distance_between(pt1,pt2):
   return math.sqrt((pt1.x-pt2.x)**2+(pt1.y-pt2.y)**2+(pt1.z-pt2.z)**2)


def cast_ray(ray,sphere_list,color,light,point):
   collision_pts = collisions.find_intersection_points(sphere_list,ray)
   if collision_pts != []:
      min_index = 0 
      for x in range(len(collision_pts)):
         if distance_between(ray.pt,collision_pts[x][1]) < distance_between(ray.pt,collision_pts[min_index][1]):
            min_index = x


      pt_normal = collisions.sphere_normal_at_point(collision_pts[min_index][0],collision_pts[min_index][1])

      scaled_vec = vector_math.scale_vector(pt_normal,0.01)

      translated_pt = vector_math.translate_point(collision_pts[min_index][1],scaled_vec)

      norm_pt_light = vector_math.normalize_vector(vector_math.vector_from_to(translated_pt,light.point))

      sphere_color = collision_pts[min_index][0].color 

      finish = collision_pts[min_index][0].finish 

      light_check = vector_math.dot_vector(pt_normal,norm_pt_light)

      ray_light = data.Ray(translated_pt,norm_pt_light)

      possible_shadows = collisions.find_intersection_points(sphere_list,ray_light)
      
      II_light_check = light_check*2

      II_norm_light_check = vector_math.scale_vector(pt_normal,II_light_check)

      vec_eye_to_Pe = vector_math.normalize_vector(vector_math.vector_from_to(point,translated_pt))

      spec_intensity = vector_math.dot_vector(vec_eye_to_Pe,II_norm_light_check)

      R = light_check * light.color.r * collision_pts[min_index][0].color.r * finish.diffuse
      G = light_check * light.color.g * collision_pts[min_index][0].color.g * finish.diffuse
      B = light_check * light.color.b * collision_pts[min_index][0].color.b * finish.diffuse
      R_spec = light.color.r * collision_pts[min_index][0].finish.specular*(spec_intensity**(1/collision_pts[min_index][0].finish.roughness))
      G_spec = light.color.g * collision_pts[min_index][0].finish.specular*(spec_intensity**(1/collision_pts[min_index][0].finish.roughness))
      B_spec = light.color.b * collision_pts[min_index][0].finish.specular*(spec_intensity**(1/collision_pts[min_index][0].finish.roughness))
      C = color_finish(color_mult(sphere_color,color),finish.ambient)

      if light_check > 0 and possible_shadows == []:
         if spec_intensity > 0:
            C.r = C.r + R_spec
            C.g = C.g + G_spec
            C.b = C.b + B_spec 
         return data.Color(C.r +R, C.g + G, C.b +B)
      else:
         return color_finish(color_mult(sphere_color,color),finish.ambient)
   else:
      return data.Color(1.0,1.0,1.0)


def pix_list(min,max,delta):
   L = []
   if min < max:
      while min<max:
         L.append(min)
         min = min + delta
      return L
   elif min > max:
      while min>max:
         L.append(min)
         min = min + delta
      return L 

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,acolor,light):

   image = open("image.ppm", "w")
 
   image.write("P3\n")
   image.write(str(width)+" " + str(height)+"\n")
   image.write("255\n")



   delta_y = (min_y - max_y)/float(height)
   delta_x = (max_x - min_x)/float(width)

   for y in pix_list(max_y, min_y, delta_y):
      for x in pix_list(min_x, max_x, delta_x):
          pix_pt = data.Point(x,y,0)
          eye_dir = vector_math.difference_point(pix_pt,eye_point)
          eye_ray = data.Ray(eye_point,eye_dir)
          color = cast_ray(eye_ray,sphere_list,acolor,light,eye_point)
          red = min(int(255*color.r),255)
          green = min(int(255*color.g),255)
          blue = min(int(255*color.b),225)

          image.write(str(red)+" "+str(green)+" "+str(blue)+ "\n")




