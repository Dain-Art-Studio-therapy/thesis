import data
import math
import vector_math

def sphere_intersection_point(ray,sphere):
    
    a= vector_math.dot_vector(ray.dir,ray.dir) 
   
    diffVec= vector_math.scale_vector(vector_math.difference_point(ray.pt,sphere.center),2)
    b= vector_math.dot_vector(diffVec,ray.dir)
    
    tempVec1= vector_math.difference_point(ray.pt,sphere.center)
    tempVec2=vector_math.difference_point(ray.pt,sphere.center)
    c= (vector_math.dot_vector(tempVec1,tempVec2)-(sphere.radius**2))
    
    tf=0 
    #calculate discriminant
    d=(b**2)-(4*a*c)
    
    if d>=0 :
       
       t1=(-b-math.sqrt(d))/(2*a)
       t2=(-b+math.sqrt(d))/(2*a)
       
    else:
    	return None

    
    if((t1<0) and (t2<0)):
        return None

    if ((t1>=0) and (t2>=0)):
    	if (t1>t2):
    		tf=t2
        else:
        	tf=t1

    elif (t1<0):
       tf=t2
    else:
       tf=t1
    
    pt=vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,tf)))
  
    return pt
    
def find_intersection_points(sphere_list,ray):
    inter_list= []
    
    if sphere_list==[]:
    	return []
    
    for n in sphere_list:
        if sphere_intersection_point(ray,n)!= None:
    	   tup= (n,sphere_intersection_point(ray,n))
           inter_list.append(tup)

    return inter_list

def sphere_normal_at_point(sphere,point):
    vec=vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))
    return vec   
  

