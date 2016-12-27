from collisions import *
from data import * 
import math 
from vector_math import *


def point_distance(point1,point2):

    return( math.sqrt( (point1.x-point2.x) ** 2 + (point1.y - point2.y) **2 +
                     (point1.z - point2.z) ** 2) )




def cast_ray(ray,sphere_list,ambcolor,Light,eye_point):

      
      A = find_intersection_points(sphere_list,ray)
    
      if A !=[]:    
      
         Distances = [ point_distance(ray.pt,tuple[1] ) for tuple in A ]
         nearest = 0
         for i in range(len(Distances)):
          
            if Distances[i] < Distances[nearest]:
               nearest = i 
         #Diffuse
         Normal_vec = sphere_normal_at_point(A[nearest][0],A[nearest][1])
         Short_vec = scale_vector(Normal_vec,.01)
         PtE = translate_point(A[nearest][1],Short_vec)
         L_dir = normalize_vector(vector_from_to(PtE,Light.pt))
         visible = dot_vector(Normal_vec,L_dir)
         ray_sphereCheck = Ray(PtE,L_dir)
         obscure_check = (find_intersection_points(sphere_list,ray_sphereCheck))
         
         diffuse_constant =( visible * A[nearest][0].finish.diffuse)
         diffuseR =( Light.color.r * A[nearest][0].color.r * diffuse_constant )
         diffuseG =( Light.color.g * A[nearest][0].color.g * diffuse_constant )
         diffuseB =( Light.color.b * A[nearest][0].color.b * diffuse_constant )
        
         #Specular         
         sc_visible = scale_vector(Normal_vec,( 2.0 * visible))
         reflect_vec = difference_vector(L_dir,(sc_visible))
         v_dir = normalize_vector(vector_from_to(eye_point,PtE))
         spec_intensity = dot_vector(reflect_vec,v_dir)
         
         specIntense_C=((spec_intensity ** (1/(A[nearest][0].finish.roughness)))
                         * A[nearest][0].finish.specular )                 
         specIntenseR = Light.color.r  * specIntense_C
         specIntenseG = Light.color.g  * specIntense_C
         specIntenseB = Light.color.b  * specIntense_C
        
         # Ambience
         fin = A[nearest][0].finish.ambient
         newColor = A[nearest][0].color
         ambR =( newColor.r * fin * ambcolor.r ) 
         ambG =( newColor.g * fin * ambcolor.g ) 
         ambB =( newColor.b * fin * ambcolor.b ) 

         if visible > 0 and obscure_check != []:

            for tuple in obscure_check:
               if point_distance(tuple[1],PtE) < point_distance(PtE,Light.pt):
                    diffuseR = 0
                    diffuseG = 0
                    diffuseB = 0
         elif visible>0 and obscure_check == []:
               pass    
               # theres diffuse compponent  
              
         elif  visible<=0:
            diffuseR = 0 
            diffuseG = 0
            diffuseB = 0

         if  spec_intensity <= 0:
            specIntenseR = 0
            specIntenseG = 0
            specIntenseB = 0

         
         
         R = ambR + diffuseR + specIntenseR
         G = ambG + diffuseG + specIntenseG
         B = ambB + diffuseB + specIntenseB

                 
         return Color(R,G,B)
      else:
         return Color(1.0,1.0,1.0) 



def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,\
                 sphere_list, ambcolor,Light):
   delta_x =( max_x-min_x)/float(width)
   delta_y = ( max_y-min_y)/float(height)
  
   print "P3"
   print width, height
   print 255

   for pt_y in range(height):
       for pt_x in range(width):
       
           vec = (difference_point(Point(min_x + (pt_x * delta_x) ,
                  max_y - (pt_y* delta_y),0 ),eye_point) )
           new_ray = Ray(eye_point,vec)

           Ncolor =  cast_ray(new_ray,sphere_list,ambcolor,Light,eye_point)
           if Ncolor.r>1:
              Ncolor.r = 1

           if  Ncolor.g>1:
               Ncolor.g = 1

           if Ncolor.b>1:
               Ncolor.b = 1
         
           print int(Ncolor.r * 255) , int(Ncolor.g * 255) , int(Ncolor.b * 255)
  
           
   
 
