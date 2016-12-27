import collisions
import data
import vector_math
import math

def distance(pt1,pt2):
   return math.sqrt((pt2.x - pt1.x) ** 2 +
                    (pt2.y - pt1.y) ** 2 +
                    (pt2.z - pt1.z) ** 2)

def float_to_ppm(sphere_color):
   return data.Color((int(round(sphere_color.r * 255))),
                     (int(round(sphere_color.g * 255))),
                     (int(round(sphere_color.b * 255))))

def find_pt_off_sphere(inter_point,normal):
   vect = vector_math.scale_vector(normal, 0.01)
   return vector_math.translate_point(inter_point,vect)

def get_diffuse_contribution(sphere,light,ray,inter_list,normal,
                             l_dir,off_pt):
   dot = vector_math.dot_vector(normal,l_dir)
   diffuse = sphere.finish.diffuse
   def calculate_contribution(light_color_component,
                              sphere_color_component):
      return (dot*light_color_component*sphere_color_component*diffuse)   
   if inter_list == []:
      return [calculate_contribution(light.color.r,sphere.color.r),
              calculate_contribution(light.color.g,sphere.color.g),
              calculate_contribution(light.color.b,sphere.color.b)]
   else:           
      dist_pt_to_light = distance(off_pt,light.pt)
      for i in range(len(inter_list)):
         if distance(inter_list[i][1],off_pt) < dist_pt_to_light:
            return [0,0,0]
      return [calculate_contribution(light.color.r,sphere.color.r),
              calculate_contribution(light.color.g,sphere.color.g),
              calculate_contribution(light.color.b,sphere.color.b)]

def determine_diffuse_contribution(sphere,off_pt,light,normal,
                                   sphere_list,l_dir,l_dot_n):
   if l_dot_n > 0:
      ray = data.Ray(off_pt,l_dir)
      inter_list = collisions.find_intersection_points(sphere_list,ray)
      return get_diffuse_contribution(sphere,light,
                                      ray,inter_list,normal,
                                      l_dir,off_pt)         
   else:
      return [0,0,0]

def determine_specular_contribution(l_dir,l_dot_n,normal,eye_position,
                                    off_pt,light_color,sphere_finish):
   reflection_vect = vector_math.difference_vector(l_dir,
                                 vector_math.scale_vector(normal,
                                                          2 * l_dot_n))
   v_dir = vector_math.normalize_vector(
                       vector_math.vector_from_to(eye_position,off_pt))
   spec_intensity = vector_math.dot_vector(reflection_vect,v_dir)
   if spec_intensity > 0:
      def compute_spec(color_comp):
         return (color_comp * sphere_finish.specular *
                 (spec_intensity ** (1 / sphere_finish.roughness)))
      r_comp = compute_spec(light_color.r)
      g_comp = compute_spec(light_color.g)
      b_comp = compute_spec(light_color.b)
      return [r_comp,g_comp,b_comp]
   else:
      return [0,0,0]

def cast_ray(ray,sphere_list,ambient_color,light,eye_position):
   inter_list = collisions.find_intersection_points(sphere_list,
                                                           ray)
   if inter_list != []:
      mindex = 0
      for i in range(1,len(inter_list)):
         if (distance(ray.pt,inter_list[i][1]) <       
             distance(ray.pt,inter_list[mindex][1])):
            mindex = i
      result_sphere = inter_list[mindex][0]
      inter_point = inter_list[mindex][1]
      sphere_color = result_sphere.color
      sphere_finish = result_sphere.finish
      sphere_normal = collisions.sphere_normal_at_point(result_sphere,
                                                        inter_point)
      pt_off_sphere = find_pt_off_sphere(inter_point,sphere_normal)
      l_dir = vector_math.normalize_vector(
                 vector_math.vector_from_to(pt_off_sphere,
                                            light.pt))
      l_dot_n = vector_math.dot_vector(sphere_normal,l_dir)
      diffuse_list = determine_diffuse_contribution(result_sphere,
                                                    pt_off_sphere,
                                                    light,sphere_normal,
                                                    sphere_list,l_dir,
                                                    l_dot_n)
      spec_intensity = determine_specular_contribution(l_dir,l_dot_n,
                                                       sphere_normal,
                                                       eye_position,
                                                       pt_off_sphere,
                                                       light.color,
                                                       result_sphere.finish)

      result_r = ((sphere_color.r * sphere_finish.ambient * 
                   ambient_color.r) + diffuse_list[0] + spec_intensity[0])
      result_g = ((sphere_color.g * sphere_finish.ambient * 
                   ambient_color.g) + diffuse_list[1] + spec_intensity[1])
      result_b = ((sphere_color.b * sphere_finish.ambient * 
                   ambient_color.b) + diffuse_list[2] + spec_intensity[2])
      return data.Color(result_r,result_g,result_b)   
   else:
      return ambient_color

def frange(min_i,max_i,jump):
   range_list = []
   while min_i < max_i:
      range_list.append(min_i)
      min_i += jump
   return range_list

def reverse_frange(min_i,max_i,jump):
   range_list = []
   while min_i <  max_i:
      range_list.append(max_i)
      max_i = max_i - jump
   return range_list

def cast_all_rays(min_x, max_x, min_y, max_y,
                  width, height, eye_point, 
                  sphere_list,ambient_color,light):
   delta_x = (max_x - min_x) / float(width)
   delta_y = (max_y - min_y) / float(height)
   print "P3", width, height, 255, ""
   for y in reverse_frange(min_y,max_y,delta_y):
      for x in frange(min_x,max_x,delta_x):
         cr_out = cast_ray(data.Ray(eye_point,
                           vector_math.difference_point(data.Point(x,y,0),
                                                        eye_point)),
                           sphere_list,
                           ambient_color,
                           light, eye_point)
         if cr_out != data.Color(1.0,1.0,1.0):
            ppm_sphere_color = float_to_ppm(cr_out)
            print (str(ppm_sphere_color.r)+" "+
                   str(ppm_sphere_color.g)+" "+ 
                   str(ppm_sphere_color.b)+" ")   
         else:
            print (str(255)+" "+
                   str(255)+" "+
                   str(255)+" ")

