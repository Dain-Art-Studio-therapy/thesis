import collisions
import data
import vector_math
import sys
import commandline
import ray_caster

def cast_ray(ray,sphere_list,ambient,light,point):
  
    
  if  (collisions.find_intersection_points(sphere_list,ray)):
  
      interList= collisions.find_intersection_points(sphere_list,ray)
    
      minSphere=interList[0][0]
      minDist=vector_math.calc_dist( ray.pt,interList[0][1])
      interPt=interList[0][1]
      #ambient=color
     
      for n in range(len(interList)):
           
         if vector_math.calc_dist(ray.pt,interList[n][1])<minDist:
             minSphere=interList[n][0]
             interPt=interList[n][1]
             minDist=vector_math.calc_dist(ray.pt,interList[n][1])

      
      pe=calc_pe(minSphere,interPt)
      N=collisions.sphere_normal_at_point(minSphere,interPt)
      lDir=calc_ldir(pe,light.pt)
      dotProd=vector_math.dot_vector(N,lDir)
      reflVec=vector_math.difference_vector(lDir,vector_math.scale_vector(N,2*dotProd))
      vDir=vector_math.normalize_vector(vector_math.vector_from_to(point,pe))
      specDotProd=vector_math.dot_vector(reflVec,vDir)
      
      #ray to test for sphere blocking
      testRay=data.Ray(pe,lDir)
      #assignment of this variable doesn't matter because it's reassigned later.
      # addAmbient=ambient
      #make sphere list between PE and light point
      newSpList=collisions.find_intersection_points(sphere_list, testRay)


      if (dotProd > 0) and (newSpList==[]):
           finColor=calc_contr(dotProd,light.color,minSphere.color,\
           minSphere.finish.diffuse, minSphere.finish.ambient,ambient)

           if specDotProd>0:
              r=light.color.r*minSphere.finish.specular*specDotProd**(1/float(minSphere.finish.roughness))
              g=light.color.g*minSphere.finish.specular*specDotProd**(1/float(minSphere.finish.roughness))
              b=light.color.b*minSphere.finish.specular*specDotProd**(1/float(minSphere.finish.roughness))
              spec_Color= add_spec(finColor,r,g,b)
              return spec_Color
              
           return finColor
      
      finColor= color_sphere(minSphere,ambient) 
      return finColor
      
  else:     
      return data.Color(1.0,1.0,1.0)  


  

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,ambient,light):
     
     xDist= max_x-min_x
     yDist=max_y-min_y
     deltaX=(xDist/float(width))
     deltaY=(yDist/float(height))

     xIndex=0
     yIndex=0

     file=ray_caster.try_open('image.ppm','w')


     file.write("P3"+"\n")

     file.write(str(width)+" "+str(height)+"\n") 
    
     file.write("255" + "\n")

     for y in range(height):
       
        for x in range(width):

           yIndex=max_y-deltaY*y
           xIndex=min_x+deltaX*x
           pt=data.Point(xIndex,yIndex,0)
           vec=vector_math.vector_from_to(eye_point,pt)
           normVec=vector_math.normalize_vector(vec)
           r=data.Ray(eye_point,normVec)

           
           rawCol=cast_ray(r,sphere_list,ambient,light,eye_point)
           red =int(rawCol.r*255)
           green= int (rawCol.g*255)
           blue= int(rawCol.b*255)
           file.write(str(red)+" "+str(green)+" "+str(blue)+"\n")
           

           

def color_sphere(sphere,col):
    rVal=sphere.color.r*sphere.finish.ambient*col.r
    gVal=sphere.color.g*sphere.finish.ambient*col.g
    bVal=sphere.color.b*sphere.finish.ambient*col.b

    finColor=data.Color(rVal,gVal,bVal)
    
    return finColor

def calc_pe(sphere,point):
    vec=vector_math.scale_vector(collisions.sphere_normal_at_point(sphere,point),.01)
    transPt= vector_math.translate_point(point,vec)
    #this is Pe
    return transPt

def calc_ldir(point1,point2):
    vec=vector_math.normalize_vector(vector_math.vector_from_to(point1,point2))
    return vec

def calc_contr(dot,lightCol,sphereCol,diffuse,spAmbient,ambient):
     rVal=sphereCol.r*spAmbient*ambient.r+ lightCol.r*diffuse*dot
     gVal=sphereCol.g*spAmbient*ambient.g+ lightCol.g*diffuse*dot
     bVal=sphereCol.b*spAmbient*ambient.b+ lightCol.b*diffuse*dot
     finColor=data.Color(rVal,gVal,bVal)

     return finColor

def add_spec(color,r,g,b):
    rVal= color.r+r
    gVal=color.g+g
    bVal=color.b+b
    return data.Color(rVal,gVal,bVal)





           


