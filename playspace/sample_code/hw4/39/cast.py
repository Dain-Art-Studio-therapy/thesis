import collisions
import vector_math
import math
import data

def cast_ray(ray,sphere_list,color,light,point):
    intersections = collisions.find_intersection_points(sphere_list,ray)
    
    if intersections != []:

        for i in intersections:
            sphere = i[0]
            intersection = i[1]
            min_dist = vector_math.length_vector(vector_math.vector_from_to(ray.pt,intersection))
            l = vector_math.length_vector(vector_math.vector_from_to(ray.pt,i[1]))
            
            if (l < mind_dist):
                sphere = i[0]
                intersection = i[1]
                min_dist = l
# Diffuse

        N = collisions.sphere_normal_at_point(sphere,intersection)
        scale_vector = vector_math.scale_vector(N,.01)
        Pe = vector_math.translate_point(intersection,scaled_vector)
        
        light_vector = vector_math.vector_from_to(Pe,light.pt)
        Ldir = vector_math.normalize_vector(light_vector)
        L_dot_N = vector_math.dot_vector(N,Ldir)
        
        light_ray = data.Ray(Pe,Ldir)
        light_intersection = collisions.find_intersection_points(sphere_list,light_ray)
        light_dist = vector_math.length_vector(light_vector)
        
        diffuse = True

        if L_dot_N > 0:
            
            if light_intersection != []:
                
                for sphere_point in light_intersections:
                    pt = sphere_point[1]
                    length_diffs = vector_math.length_vector(vector_math.difference_point(pt,Pe))
                    
                    if length_diffs < light_dist:
                        diffuse = False

        else:
            diffuse = False

# Specular Vals

        Nscaled = vector_math.scale_vector(N,(2 * L_dot_N))
        reflection_vector = vector_math.difference_vector(Ldir,Nscaled)
        Vdir = vector_math.normalize_vector(vector_math.difference_point(Pe,pt))
        specular_intensity = vector_math.dot_vector(reflection_vector,Vdir)

        if specular_intensity > 0:
            
            s_specular = sphere.finish.specular
            s_rough = sphere.finish.rough
            
            r = (light.color.r * s_specular) * (specular_intnsity ** (1/float(s_rough)))
            g = (light.color.g * s_specular) * (specular_intnsity ** (1/float(s_rough)))
            b = (light.color.b * s_specular) * (specular_intnsity ** (1/float(s_rough)))

        else:
            r = 0
            g = 0
            b = 0


        if diffuse:
            L_r = light.color.r
            L_g = light.color.g
            L_b = light.color.b
            s_r = sphere.color.r
            s_g = sphere.color.g
            s_b = sphere.color.b

            diffuse_r = (L_dot_N * L_r * s_r * sphere.finish.diffuse)
            diffuse_g = (L_dot_N * L_g * s_g * sphere.finish.diffuse)
            diffuse_b = (L_dot_N * L_b * s_b * sphere.finish.diffuse)

        else:
            diffuse_r = 0
            diffuse_g = 0
            diffuse_b = 0

        s_color = sphere.color
            
        finalR = color.r * s_color.r * sphere.finish.ambient + diffuse_r + r
        finalG = color.g * s_color.g * sphere.finish.ambient + diffuse_g + g
        finalB = color.b * s_color.b * sphere.finish.ambient + diffuse_b + b

        Fcolor = data.Color(finalR,finalG,finalB)

        return Fcolor

    else:
        return data.Color(1.0,1.0,1.0)         


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,color,light):

    xlength = max_x - min_x
    dx = xlength/width
    xvals = [min_x + (x*dx) for x in range(width)]

    ylength = max_y - min_y
    dy = ylength/height  
    yvals = [max_y - (y*dx) for y in range(height)]
    
    for y in yvals:
        for x in xvals:
            vector = vector_math.vector_from_to(eye_point,data.Point(x,y,0))
            color = cast_ray(data.Ray(eye_point,vector),sphere_list,color,light,eye_point)
            if color:
                print int(color.r**255),int(color.g**2),int(color.b**2)
            else:
                print "255 255 255"          


#def color_bound(r,b,g):
#    if r > 255:
#        print 255
#    if b > 255:
#        print 255
#    if g > 255:
#        print 255

