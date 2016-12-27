import collisions
import math
import data
import vector_math

def cast_ray(ray,sphere_list,color,light,eye):
   S = collisions.find_intersection_points(sphere_list,ray)
   if S == []:
      return data.Color(1.0,1.0,1.0)
   else:
      nearest = 0
      for i in range(len(S)):
         L = vector_math.length_vector(vector_math.difference_point(S[i][1],ray.pt))
         L2 = vector_math.length_vector(vector_math.difference_point(S[nearest][1],ray.pt))
         if L < L2:
            nearest = i
      N = collisions.sphere_normal_at_point(S[nearest][0],S[nearest][1])

      p = vector_math.translate_point(S[nearest][1],vector_math.scale_vector(N,.01))   

      L = vector_math.normalize_vector(vector_math.difference_point(light.pt,p))
  
      dot = vector_math.dot_vector(N,L)

      ref = vector_math.difference_vector(L,vector_math.scale_vector(N,2*dot))
   
      V = vector_math.normalize_vector(vector_math.difference_point(p,eye))
   
      specintens = vector_math.dot_vector(V,ref)
  
      if dot > 0 and collisions.find_intersection_points(sphere_list,data.Ray(p,L)) == []:
         diffr = vector_math.dot_vector(N,L)*light.color.R*S[nearest][0].color.R*S[nearest][0].finish.diffuse
      
         diffg = vector_math.dot_vector(N,L)*light.color.G*S[nearest][0].color.G*S[nearest][0].finish.diffuse

         diffb = vector_math.dot_vector(N,L)*light.color.B*S[nearest][0].color.B*S[nearest][0].finish.diffuse
      else:
         diffr = 0
         diffg = 0
         diffb = 0

      if specintens > 0:
         specr = light.color.R*S[nearest][0].finish.specular*(specintens)**(1/S[nearest][0].finish.roughness)

         specg = light.color.G*S[nearest][0].finish.specular*(specintens)**(1/S[nearest][0].finish.roughness)
        
         specb = light.color.B*S[nearest][0].finish.specular*(specintens)**(1/S[nearest][0].finish.roughness)

      else:
         specr = 0
         specg = 0
         specb = 0

      r = S[nearest][0].color.R * S[nearest][0].finish.ambient * color.R + diffr + specr
      
      g = S[nearest][0].color.G * S[nearest][0].finish.ambient * color.G + diffg + specg
      
      b = S[nearest][0].color.B * S[nearest][0].finish.ambient * color.B + diffb + specb
      
      c = data.Color(r,g,b)
     
      return c
  
      

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light):
   
   for y in range(0,height):
      yd = (max_y-min_y)/float(height)
      for x in range(0,width):
         xd = (max_x-min_x)/float(width)
         p = data.Point((min_x+x*xd),(max_y-y*yd),0) 
         v = vector_math.normalize_vector(vector_math.difference_point(p,eye_point))
         R = data.Ray(eye_point,v)
         c = cast_ray(R,sphere_list,color,light,eye_point)
         
         print min(255,int(c.R*255)), min(255,int(c.G*255)), min(255,int(c.B*255))
 
            
         

   
