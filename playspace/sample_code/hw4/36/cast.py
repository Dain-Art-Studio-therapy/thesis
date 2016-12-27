import collisions
import data
import vector_math


def cast_ray(ray,sphere_list,color):
  
    
  if  (collisions.find_intersection_points(sphere_list,ray)):
  
      interList= collisions.find_intersection_points(sphere_list,ray)
    
      minSphere=interList[0][0]
      minDist=vector_math.calc_dist( ray.pt,interList[0][1])
      for n in range(len(interList)):
         if vector_math.calc_dist(ray.pt,interList[n][1])<minDist:
             minSphere=interList[n][0]
             minDist=vector_math.calc_dist(ray.pt,interList[n][1])
      
      finColor= dark_sphere(minSphere,color) 
      return finColor

  else: 
       return data.Color(1.0,1.0,1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,color):
     
     xDist= max_x-min_x
     yDist=max_y-min_y
     deltaX=(xDist/float(width))
     deltaY=(yDist/float(height))

     xIndex=0
     yIndex=0
     
     print 'P3'
     print width, height
     print 255

     for y in range(height):
       
        for x in range(width):

           yIndex=max_y-deltaY*y
           xIndex=min_x+deltaX*x
           pt=data.Point(xIndex,yIndex,0)
           vec=vector_math.vector_from_to(eye_point,pt)
           normVec=vector_math.normalize_vector(vec)
           r=data.Ray(eye_point,normVec)

           
           rawCol=cast_ray(r,sphere_list,color)
           red =int(rawCol.r*255)
           green= int (rawCol.g*255)
           blue= int(rawCol.b*255)
           print red,green,blue

           

def dark_sphere(sphere,col):
    rVal=sphere.color.r*sphere.finish.ambient*col.r
    gVal=sphere.color.g*sphere.finish.ambient*col.g
    bVal=sphere.color.b*sphere.finish.ambient*col.b

    finColor=data.Color(rVal,gVal,bVal)
    
    return finColor
           


