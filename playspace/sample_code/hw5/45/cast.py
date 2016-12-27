# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09

import utility
import data
import vector_math
import math
import collisions
import sys
import commandline

def dist(ray,sphere_point):
    return vector_math.length_vector(
        vector_math.difference_point(ray.pt,sphere_point))

def distance(point,sphere_point):
    return vector_math.length_vector(
        vector_math.difference_point(point,sphere_point))

def colorprint(color):
    #formats the color into a [0,255] range and prints the string.
    #if the color is greater than 1.0 then it defaults to 255 (caps at 255).
    
    colorr = int(color.r*255) if color.r<1.0 else 255
    colorg = int(color.g*255) if color.g<1.0 else 255
    colorb = int(color.b*255) if color.b<1.0 else 255

    print colorr, colorg, colorb

def cast_ray(ray, sphere_list,color,light,eye_point):
    shadow = False
    intersects = collisions.find_intersection_points(sphere_list,ray)

    if not intersects:
        return data.Color(1.0,1.0,1.0)
    
    else:
        diffuser = 0
        diffuseg = 0
        diffuseb = 0
        specr = 0
        specg = 0
        specb = 0
        i_dist = []
        for points in intersects:
            i_dist.append((dist(ray,points[1]),
                           points[0].color,
                           points[0].finish,
                           points[0],
                           points[1]))
            
        #i_dist: 0:distance 1:color 2:finish 3:sphere 4:intersection point
    
        idx = i_dist.index(min(i_dist))
        spherecolor = i_dist[idx][1]
        spherefinish = i_dist[idx][2]
        
        N = collisions.sphere_normal_at_point(i_dist[idx][3],i_dist[idx][4])
        
        Pe = vector_math.translate_point(i_dist[idx][4],
                                        vector_math.scale_vector(N,0.01))
        
        Ldir = vector_math.normalize_vector(
            vector_math.vector_from_to(Pe,light.pt))
        
        dot = vector_math.dot_vector(N,Ldir)
        
        reflection_vector = vector_math.normalize_vector(
            vector_math.difference_vector(Ldir,
                                          vector_math.scale_vector(N,2*dot)))
        
        Vdir = vector_math.normalize_vector(
            vector_math.vector_from_to(eye_point,Pe))
        
        specular_intensity = vector_math.dot_vector(
            reflection_vector,Vdir)
        
        # ray from Pe to the direction of Ldir
        lightray = data.Ray(Pe,Ldir)
        
        #check if it collides with a sphere closer to Pe than the light is.
        intersects2 = collisions.find_intersection_points(sphere_list,lightray)
        
        # this is the list of collisions
        i_dist2=[]
        for point in intersects2:
            i_dist2.append((dist(lightray,point[1])))
            #appends to an array the distances between Pe
            #and the current colliding intersection
            
        if intersects2:
            smallest = min(i_dist2)
            if smallest < distance(Pe,light.pt):
                shadow = True
            #checks the minimum distance with the between Pe
            #and the light source's point.
            
        if dot>0:
            if not shadow:
               # if distance(Pe,points[4])<distance(Pe,light.pt):
                diffuser = dot*light.color.r*spherecolor.r*spherefinish.diffuse
                diffuseg = dot*light.color.g*spherecolor.g*spherefinish.diffuse
                diffuseb = dot*light.color.b*spherecolor.b*spherefinish.diffuse

        if specular_intensity>0:
            # doesn't add the specular if it's obstructed.
            if dot>0:
                spec = specular_intensity**(1/spherefinish.roughness)
                specr = light.color.r*spherefinish.specular*spec
                specg = light.color.g*spherefinish.specular*spec
                specb = light.color.b*spherefinish.specular*spec
            else:
                specr = 0
                specg = 0
                specb = 0
                                            
        red = spherecolor.r*color.r*spherefinish.ambient+diffuser+specr
        green = spherecolor.g*color.g*spherefinish.ambient+diffuseg+specg
        blue = spherecolor.b*color.b*spherefinish.ambient+diffuseb+specb

        returncolor = data.Color(red,green,blue)
        return returncolor
                
def cast_all_rays(min_x,max_x,min_y,max_y,
                  width,height,eye_point,
                  sphere_list,color,light):
    
    width_bound = (max_x-min_x)/float(width)
    height_bound = (max_y-min_y)/float(height)

    px = []
    y = max_y
    while (y > min_y):
        x = min_x
        
        while (x < max_x):
            
            point = data.Point(x, y, 0.0)
            vector = vector_math.vector_from_to(eye_point, point)
            ray = data.Ray(eye_point,vector)
            px.append(ray)
            # add the point to the px array
            
            x+=width_bound
        y-=height_bound

        sys.stdout = open("image.ppm",'w')

        print "P3"
        print width,height
        print 255
        
    for each_ray in px:
        colorfinal = cast_ray(each_ray, sphere_list,color,light,eye_point)
        print colorprint(colorfinal)



