import data
import vector_math
import math

def quadradic(a,b,c,isPos):

    if isPos:
        return (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    else:
        return (-b - math.sqrt(b**2-(4*a*c)))/(2*a)

def sphere_intersection_point(ray,sphere):

    d = vector_math.difference_point(ray.pt,sphere.center)
    a = vector_math.dot_vector(ray.dir,ray.dir)
    b = vector_math.dot_vector(vector_math.scale_vector(d,2),ray.dir)
    c = vector_math.dot_vector(d,d)- sphere.radius**2

    if b**2-(4*a*c) < 0:

        return None

    elif quadradic(a,b,c,True) < 0 and quadradic(a,b,c,False) < 0:

        return None

    elif quadradic(a,b,c,True) < 0 and quadradic(a,b,c,False) >= 0:

        return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir,quadradic(a,b,c,False)))

    elif quadradic(a,b,c,True) >= 0 and quadradic(a,b,c,False) < 0:

        return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir,quadradic(a,b,c,True)))

    elif quadradic(a,b,c,True) >= 0 and quadradic(a,b,c,False) >= 0:
        
        if quadradic(a,b,c,True) <= quadradic(a,b,c,False):

            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir,quadradic(a,b,c,True)))
        
        else:

            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir,quadradic(a,b,c,False)))

def find_intersection_points(sphere_list,ray):

    new_slist = []

    for s in range (0, len(sphere_list)):

        inpnt = sphere_intersection_point(ray,sphere_list[s])

        if inpnt != None:

            new_slist.append( (sphere_list[s],inpnt) )

    return new_slist

def sphere_normal_at_point(sphere,point):

    nap = vector_math.vector_from_to(sphere.center,point)

    return vector_math.normalize_vector(nap)
    

        
        

