import collisions
import data
import vector_math


def distance(list,ray):
   distance = []
   for i in list:
      distance.append(vector_math.length_vector(vector_math.vector_from_to(i[1],ray.pt)))
   return distance



def cast_ray(ray,sphere_list,ambi,light):
   answer = collisions.find_intersection_points(sphere_list,ray)  
   distanceans = []
   if answer == []:
      return (255,255,255)
   else:
      new_list = distance(answer,ray)
      minimum = new_list.index(min(new_list))
      return answer[minimum][0].color


 

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,ambi,light):
   print "P3"
   print width, height
   print 255

   for y in xrange(height):
      point_y = max_y - ((max_y - min_y) / float(height)) * y
      for x in xrange(width):
         point_x = min_x + ((max_x - min_x) / float(width)) * x
         casted_ray = data.Ray(eye_point, vector_math.vector_from_to (eye_point, data.Point(point_x,point_y,0)))
         casted = cast_ray(casted_ray, sphere_list,ambi,light)
         
         answer = collisions.find_intersection_points(sphere_list,casted_ray)

         if answer != []:
            new_list = distance(answer,casted_ray)
            intersect = answer[new_list.index(min(new_list))]      
            N = vector_math.normalize_vector( vector_math.vector_from_to(intersect[0].center,intersect[1]))
            P = vector_math.translate_point(intersect[1], vector_math.scale_vector( N, 0.01))
            L = vector_math.normalize_vector( vector_math.vector_from_to(P, light.pt))
            Dot2 = vector_math.dot_vector(N,L)
            Ray2 = data.Ray(P, vector_math.vector_from_to(P,L))
            C = collisions.sphere_intersection_point(Ray2,intersect[0])           
            if C != None:
               A = vector_math.dot_vector(N, vector_math.normalize_vector(L))        
               CL = vector_math.length_vector(vector_math.vector_from_to(C,L))
               CP = vector_math.length_vector(vector_math.vector_from_to(C,P))
            for i in sphere_list:
               if i.color == casted:
                  correct_sphere = i

            if (Dot2 <= 0) or (not(C != None)) or (CL > CP):
               dot_product = 1 

            else:
               dot_product = A
    
         else:
            dot_product = 1
   
         if casted != (255,255,255):
            print int(correct_sphere.color.r * correct_sphere.finish.diffuse *  dot_product * light.color.r) + (ambi.r * correct_sphere.color.r)
            print int(correct_sphere.color.g * correct_sphere.finish.diffuse * dot_product * light.color.g) + (ambi.g * correct_sphere.color.g)
            print int(correct_sphere.color.b * correct_sphere.finish.diffuse * dot_product * light.color.b) + (ambi.b * correct_sphere.color.b)
 
         else:
            print 255 , "\n" , 255 , "\n" , 255


