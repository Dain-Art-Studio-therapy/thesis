import collisions
import vector_math
import data
import utility

MAX_COLOR_NUM = 255

def cast_ray(ray, sphere_list,amb,light,eyepoint):
   ls = collisions.find_intersection_points(sphere_list,ray)
   if ls == []:
      return data.Color(1.0,1.0,1.0)
   else:
      d = vector_math.length_vector(vector_math.vector_from_to(
         ray.pt, ls[0][1]))
      sph = ls[0][0]
      p = ls[0][1] 
      for i in range(1, len(ls)):
         temp_d = vector_math.length_vector(vector_math.vector_from_to(
                                           ray.pt, ls[i][1]))
         if temp_d < d:
            d = temp_d
            sph = ls[i][0]
            p = ls[i][1]
      return compute_color(sph,p,sphere_list,amb,light,eyepoint)

      
def compute_color(sphere,point,sphere_list,ambient,light,eyepoint):
   light_component = compute_light(sphere,point,light,sphere_list,eyepoint)
   ambient_component = compute_ambient(sphere,ambient)
   c = color_add(ambient_component, light_component)
   return c

def compute_spec(light,sphere,ldir,n,ldotn,eyepoint,pe):
   ref_v = vector_math.difference_vector(ldir,vector_math.scale_vector(n,2*ldotn))
   vdir = vector_math.normalize_vector(vector_math.vector_from_to(eyepoint,pe))
   spec_inten = vector_math.dot_vector(ref_v,vdir)   
   if spec_inten > 0:
      return data.Color(light.color.r*sphere.finish.specular*(spec_inten**(1/sphere.finish.roughness)),
                             light.color.g*sphere.finish.specular*(spec_inten**(1/sphere.finish.roughness)),
                             light.color.b*sphere.finish.specular*(spec_inten**(1/sphere.finish.roughness)))
   else:
      return data.Color(0.0,0.0,0.0)

def compute_light(sphere,point,light,sphere_list,eyepoint):
   n = collisions.sphere_normal_at_point(sphere,point)
   pe = vector_math.translate_point(point,
      vector_math.scale_vector(vector_math.normalize_vector(n),.01))
   ldir = vector_math.normalize_vector(
      vector_math.vector_from_to(pe,light.pt))
   ldotn = vector_math.dot_vector(n,ldir)
   if ldotn <= 0:
      return data.Color(0.0,0.0,0.0)
   inline = collisions.find_intersection_points(sphere_list,data.Ray(pe,ldir))   
   if not(sphere_before_light(inline,light,pe)):
      specular_component = compute_spec(light,sphere,ldir,n,ldotn,eyepoint,pe)
      diffuse_component = compute_diffuse(ldotn,light,sphere)
      return color_add(specular_component,diffuse_component)
   else:
      return data.Color(0.0,0.0,0.0)

def sphere_before_light(intersections,light,point):
   for e in intersections:
      if dist_squared(e[1],point) < dist_squared(light.pt,point):
         return True
   return False

def compute_diffuse(dot,light,sphere):
   return data.Color(dot * light.color.r * sphere.color.r * sphere.finish.diffuse,
                     dot * light.color.g * sphere.color.g * sphere.finish.diffuse,
                     dot * light.color.b * sphere.color.b * sphere.finish.diffuse) 

def compute_ambient(sphere,ambient):
   return data.Color(sphere.color.r * sphere.finish.ambient * ambient.r,
                     sphere.color.g * sphere.finish.ambient * ambient.g,
                     sphere.color.b * sphere.finish.ambient * ambient.b)

def color_add(c1,c2):
   return data.Color(c1.r + c2.r,c1.g + c2.g,c1.b + c2.b)

def dist_squared(p1,p2):
   return (p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2

def crange(start,stop,step):
   ls = []
   a = start

   if step > 0:
      while a < stop:
         ls.append(a)
         a += step
      return ls
   elif step < 0:
      while a > stop:
         ls.append(a)
	 a += step
      return ls
   # else return none

def ceiling_of(x,y):
   if x > y:
      return y
   else:
      return x

def cast_all_rays(min_x,max_x,min_y,max_y,width,
                  height,eye_point,sphere_list,amb,light):
   pixel_list = ['P3',width,height,MAX_COLOR_NUM]

   x_inc = float(max_x - min_x) / float(width)
   y_inc = float(min_y - max_y) / float(height)
   
   for j in crange(max_y,min_y,y_inc):
      for i in crange(min_x,max_x,x_inc):
         r1 = data.Ray(eye_point, vector_math.vector_from_to(
                      eye_point,data.Point(i,j,0)))
         c1 = cast_ray(r1, sphere_list,amb,light,eye_point)
         ctriple = process_color(c1)
         pixel_list.append(ctriple[0])
         pixel_list.append(ctriple[1])
         pixel_list.append(ctriple[2])

   return pixel_list

def process_color(c):
         return (ceiling_of(int(round(MAX_COLOR_NUM*c.r)),MAX_COLOR_NUM), 
                 ceiling_of(int(round(MAX_COLOR_NUM*c.g)),MAX_COLOR_NUM), 
                 ceiling_of(int(round(MAX_COLOR_NUM*c.b)),MAX_COLOR_NUM))



