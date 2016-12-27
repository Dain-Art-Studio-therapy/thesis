import vector_math
import collisions
import data
import utility
import sys

def cast_ray(ray,sphere_list,lcol,light,eye): #returns colors, of all things, useless, this is 
    clist = collisions.find_intersection_points(sphere_list,ray)

    if len(clist) == 0:
        return data.Color(1.0,1.0,1.0) #
    else:
        return closest_color(clist,ray.pt,lcol,light,sphere_list,eye)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,lcol,light):

    #funtions by printing all pixels to a new line under the P3 Header

    #//header
    print "P3"
    print width, height
    print "255"

    #change in x or y
    dx = (float(max_x) - min_x)/width
    dy = (float(max_y) - min_y)/height

    for i in range (0 , height): #y

        y = max_y - (dy*i)
        
        for j in range (0 , width): #x

            x = min_x + (dx*j)
            
            
            r = data.Ray(eye_point,
                         vector_math.vector_from_to(eye_point,data.Point(x,y,0.0)))

            #ray at eye point with vector from eye to point @ above

            pixel = cast_ray(r,sphere_list,lcol,light,eye_point)

            if pixel.r > 1:
                pixel.r = 1
            if pixel.g > 1:
                pixel.g = 1
            if pixel.b > 1:
                pixel.b = 1
                
            print int(pixel.r*255) , int(pixel.g*255) , int(pixel.b*255)


def closest_color(inlist,pt,lcol,light,slist,eye): #finds colors because I'm bad || if you want test cases for this I'll impliment it into
                                  #cast ray because I hate test cases and I know it works
    mindex = 0

    for i in range (len(inlist)):
        #if i != 0:
            #print >> sys.stderr, inlist[i][1].x, inlist[i][1].y, inlist[i][1].z
            #print >> sys.stderr, inlist[mindex][1].x, inlist[mindex][1].y, inlist[mindex][1].z
            #print >> sys.stderr, utility.distance_3d(pt,inlist[i][1]), utility.distance_3d(pt,inlist[mindex][1])
        if utility.distance_3d(pt,inlist[i][1]) <= utility.distance_3d(pt,inlist[mindex][1]):
                mindex = i

    oldc = data.Color(inlist[mindex][0].color.r*inlist[mindex][0].finish.amb*lcol.r,
                      inlist[mindex][0].color.g*inlist[mindex][0].finish.amb*lcol.g,
                      inlist[mindex][0].color.b*inlist[mindex][0].finish.amb*lcol.b)
    return lit_color(inlist[mindex],lcol,light,slist,oldc,eye)




def lit_color(coltup,lcol,light,slist,oldc,eye):
    #computes colors featuring diffuse, lights, and a bunch of other worthless crap
    #takes data in the form (sphere,point),finish,lcol,light

    #compute pe
    snorm = snorm = collisions.sphere_normal_at_point(coltup[0],coltup[1])
    pe = vector_math.translate_point(coltup[1],vector_math.scale_vector(snorm,0.01))

    #check light compared to pe on sphere
    lvec = vector_math.normalize_vector(vector_math.vector_from_to(pe,light.pt))
    if vector_math.dot_vector(snorm,lvec) > 0:
        #checks if there's another sphere in the way
        rcheck = data.Ray(pe,lvec)
        clist = collisions.find_intersection_points(slist,rcheck)
        if is_closest_collision(coltup,clist,light):
            newc = data.Color(vector_math.dot_vector(lvec,snorm)*light.col.r*coltup[0].color.r*coltup[0].finish.diff,
                              vector_math.dot_vector(lvec,snorm)*light.col.g*coltup[0].color.g*coltup[0].finish.diff,
                              vector_math.dot_vector(lvec,snorm)*light.col.b*coltup[0].color.b*coltup[0].finish.diff)
            return specular(data.Color(newc.r+oldc.r,newc.g+oldc.g,newc.b+oldc.b),lvec,vector_math.dot_vector(lvec,snorm),snorm,eye,pe,coltup,light)
    
    return data.Color(oldc.r,oldc.g,oldc.b)
        #specular(data.Color(oldc.r,oldc.g,oldc.b),lvec,vector_math.dot_vector(lvec,snorm),snorm,eye,pe,coltup,light)


def is_closest_collision(coltup,clist,light):
    for i in range(len(clist)):
        if utility.distance_3d(clist[i][1],coltup[1]) < utility.distance_3d(coltup[1],light.pt):
            return False
    return True

def specular(color,ldir,ldn,snorm,eye,pe,coltup,light):
    rvec = vector_math.difference_vector(ldir,vector_math.scale_vector(snorm,2*ldn))
    neye = vector_math.normalize_vector(vector_math.vector_from_to(eye,pe))
    si = vector_math.dot_vector(rvec,neye)
    if si > 0:
        #print >> sys.stderr, color.r+(light.col.r*coltup[0].finish.spec*(si**(1.0/coltup[0].finish.rough))*coltup[0].finish.spec)
        #print >> sys.stderr, color.g+(light.col.r*coltup[0].finish.spec*(si**(1.0/coltup[0].finish.rough))*coltup[0].finish.spec)
        #print >> sys.stderr, color.b+(light.col.r*coltup[0].finish.spec*(si**(1.0/coltup[0].finish.rough))*coltup[0].finish.spec)
                                      
        return data.Color(color.r+(light.col.r*coltup[0].finish.spec*(si**(1.0/coltup[0].finish.rough))),
                          color.g+(light.col.g*coltup[0].finish.spec*(si**(1.0/coltup[0].finish.rough))),
                          color.b+(light.col.b*coltup[0].finish.spec*(si**(1.0/coltup[0].finish.rough))))
    return data.Color(color.r,color.g,color.b)
                          
    
        
    


         
        
        
    
    
    
                      
                
                
                

    

    

    
    


    
