import collisions
import vector_math
import data
import utility

MAX_COLOR_NUM = 255

def cast_ray(ray, sphere_list,amb,light,eyepoint):
   c = data.Color(1.0,1.0,1.0)
   ls = collisions.find_intersection_points(sphere_list,ray)
   if ls == []:
      pass
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
      n = collisions.sphere_normal_at_point(sph,p)
      pe = vector_math.translate_point(p,
                vector_math.scale_vector(vector_math.normalize_vector(n),.01))
      ldir = vector_math.normalize_vector(
                vector_math.vector_from_to(pe,light.pt))
      ldotn = vector_math.dot_vector(n,ldir)
      inline = collisions.find_intersection_points(
                sphere_list,data.Ray(pe,ldir))
      ref_v = vector_math.difference_vector(ldir,vector_math.scale_vector(n,2*ldotn))
      vdir = vector_math.normalize_vector(vector_math.vector_from_to(eyepoint,pe))
      spec_inten = vector_math.dot_vector(ref_v,vdir)
      if spec_inten > 0:
         spec_comp = data.Color(light.color.r*sph.finish.specular*(spec_inten**(1/sph.finish.roughness)),
                                light.color.g*sph.finish.specular*(spec_inten**(1/sph.finish.roughness)),
                                light.color.b*sph.finish.specular*(spec_inten**(1/sph.finish.roughness)))
      else:
         spec_comp = data.Color(0.0,0.0,0.0)
      if inline == [] and ldotn > 0:
         lt_comp = data.Color(ldotn*light.color.r*sph.color.r*sph.finish.diffuse,
                              ldotn*light.color.g*sph.color.g*sph.finish.diffuse,
                              ldotn*light.color.b*sph.color.b*sph.finish.diffuse) 
      else:
         lt_comp = data.Color(0,0,0)
      c.r = sph.color.r * sph.finish.ambient * amb.r + lt_comp.r + spec_comp.r
      c.g = sph.color.g * sph.finish.ambient * amb.g + lt_comp.g + spec_comp.g
      c.b = sph.color.b * sph.finish.ambient * amb.b + lt_comp.b + spec_comp.b
   return c 
      

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
   print 'P3'
   print width, height
   print MAX_COLOR_NUM

   x_inc = float(max_x - min_x) / float(width)
   y_inc = float(min_y - max_y) / float(height)
   
   for j in crange(max_y,min_y,y_inc):
      for i in crange(min_x,max_x,x_inc):
         r1 = data.Ray(eye_point, vector_math.vector_from_to(
                      eye_point,data.Point(i,j,0)))
         c1 = cast_ray(r1, sphere_list,amb,light,eye_point)
         print ceiling_of(int(round(MAX_COLOR_NUM*c1.r)),MAX_COLOR_NUM), 
         # Int() to match the formatting
         print ceiling_of(int(round(MAX_COLOR_NUM*c1.g)),MAX_COLOR_NUM), 
         # of P3. Round() to try and be
         print ceiling_of(int(round(MAX_COLOR_NUM*c1.b)),MAX_COLOR_NUM), 
         # accurate to true colors.





