import collisions
import data
import vector_math
import math


def cast_ray(ray, sphere_list, amb, light, point):
    a = collisions.find_intersection_points (sphere_list, ray) #[sphere,intpt]
    
    if a != []:
        min_dist = distance_2pts(ray.pt, a[0][1])
        mindex = 0
        
        for i in range(0,len(a)):
            pt = a[i][1]
            d = distance_2pts(ray.pt, pt)
            if d < min_dist:
                min_dist = d
                mindex = i 

        r = a[mindex][0].color.r * amb.r * a[mindex][0].finish.ambient 
        g = a[mindex][0].color.g * amb.g * a[mindex][0].finish.ambient
        b = a[mindex][0].color.b * amb.b * a[mindex][0].finish.ambient

        #translate int_pt along sp_norm by 0.01
        int_pt = a[mindex][1] 
        sphere = a[mindex][0]
        N = collisions.sphere_normal_at_point(sphere,int_pt)
        scale_N = vector_math.scale_vector(N, 0.01)
        P = vector_math.translate_point(int_pt,scale_N)

        #check if light is on other side
        light_dir = vector_math.vector_from_to(P, light.pt)
        L_dir = vector_math.normalize_vector(light_dir)
        dot_prod = vector_math.dot_vector(N, L_dir)
        if dot_prod <= 0:
            sphere.finish.diffuse = 0
        else:
            #check if other sphere is between
            ray_light_sp = data.Ray(P, light_dir)
            f = collisions.find_intersection_points(sphere_list, ray_light_sp)
            if f != []:
                for i in range(len(f)):
                    dist_intpt_P = distance_2pts(f[i][1], P)
                    dist_light_P = distance_2pts(P, light.pt)
                    if dist_light_P >  dist_intpt_P:
                        sphere.finish.diffuse = 0

        #if light is not obscured
        x = sphere.color
        y = sphere.finish.diffuse
        
        r1 = dot_prod * amb.r * x.r * y
        g1 = dot_prod * amb.g * x.g * y
        b1 = dot_prod * amb.b * x.b * y

        #specular intnsity stuff
        v_scaled_dir = vector_math.scale_vector(N,(2 * dot_prod))
        reflection = vector_math.difference_vector(L_dir, v_scaled_dir)
        v_dir = vector_math.vector_from_to(point,P)
        spec_inten = vector_math.dot_vector(reflection,v_dir)

        if spec_inten <= 0:
            sphere.finish.specular = 0
            
        k = spec_inten ** (1 / sphere.finish.roughness)
        r2 = amb.r * sphere.finish.specular * k
        g2 = amb.g * sphere.finish.specular * k
        b2 = amb.b * sphere.finish.specular * k

        r_total = r+r1+r2
        g_total = g+g1+g2
        b_total = b+b1+b2

        if r_total >= 1.0:
            r_total = 1.0
        if g_total >= 1.0:
            g_total = 1.0
        if b_total >= 1.0:
            b_total = 1.0
        

        return data.Color(r_total, g_total, b_total)
    else:
        return data.Color(1.0, 1.0, 1.0)
    

def distance_2pts(pt1,pt2):
    return math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2 + (pt1.z - pt2.z)**2)
            

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    print 'P3'
    print width, height
    print 255
    for i in range(height):
        for j in range(width):
            dx = (max_x - min_x) / float(width)
            dy = (max_y - min_y) / float(height)
            pt = data.Point(min_x + j * dx , max_y - i * dy, 0)
            vec1 = vector_math.vector_from_to(eye_point, pt)
            ray = data.Ray(eye_point, vec1) 
            a = cast_ray(ray,sphere_list,color,light,eye_point)
            if a == data.Color(1.0, 1.0, 1.0):
                print 255, 255, 255
            else:
                print int(a.r * 255) , int (a.g * 255) , int (a.b * 255) 
                   
