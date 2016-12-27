from collisions import *
from data import *
from vector_math import *

def distance(p1,p2):
    return math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2)+((p1.z-p2.z)**2))

def find_smallest_index(nums):
    mindex = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[mindex]:
            mindex = i
    return mindex

def capValue(int):
    if 0.0 <= int <= 1.0:
        return int
    else:
        return 1.0

def cast_ray(ray,sphere_list,clr,Light,point):
    #Closest intersection index
    list = find_intersection_points(sphere_list,ray)
    mindex = 0
    if list != []:
        pts = [p for (s,p) in list]
        dist_list = [distance(ray.pt,pt) for pt in pts]
        mindex = find_smallest_index(dist_list)

        #Closest intersection_pt,sphere,sph_clr,ambient,diffuse,light_clr 
        sphere = list[mindex][0]
        pt = list[mindex][1]
        s_col = sphere.color
        amb = sphere.finish.ambient
        diff = sphere.finish.diffuse
        l_clr = Light.color
        rough = sphere.finish.roughness
        spec = sphere.finish.specular

        #New intersection pt
        N = normalize_vector(vector_from_to(sphere.center,pt))
        Pe = translate_point(pt,scale_vector(N,0.01))
        Ldir = normalize_vector(vector_from_to(Pe,Light.pt))
        vis = dot_vector(N,Ldir)

        #Check for closer sphere
        diff_dist = distance(Pe,Light.pt)
        diff_list = find_intersection_points(sphere_list,Ray(Pe,Ldir))

        #Specular
        reflection = difference_vector(Ldir,scale_vector(N,(2*vis)))
        Vdir = normalize_vector(vector_from_to(point,Pe))
        spec_intensity = dot_vector(reflection,Vdir)

        #Colors
        r1 = (s_col.r * amb * clr.r)
        g1 = (s_col.g * amb * clr.g)
        b1 = (s_col.b * amb * clr.b)
        shadedClr = Color(r1,g1,b1)
        r2 = r1 + (vis * l_clr.r * s_col.r * diff)
        g2 = g1 + (vis * l_clr.g * s_col.g * diff)
        b2 = b1 + (vis * l_clr.b * s_col.b * diff)
        diffuseClr = Color(r2,g2,b2)
        r3 = capValue(r2 + (l_clr.r * spec * spec_intensity**(1/rough)))
        g3 = capValue(g2 + (l_clr.g * spec * spec_intensity**(1/rough)))
        b3 = capValue(b2 + (l_clr.b * spec * spec_intensity**(1/rough)))
        specClr = Color(r3,g3,b3)

        #Return Color
        if vis > 0:
            for (s,p) in diff_list:
                pt_dist = distance(Pe,p)
                if pt_dist < diff_dist:
                    return shadedClr
            if spec_intensity > 0:
                return specClr
            return diffuseClr
        else:  
            return shadedClr
    else:
        return Color(1.0,1.0,1.0)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,clr,Light):
    dx = (max_x-min_x)/float(width)
    dy = (max_y-min_y)/float(height)

    for y in range(height):
        for x in range(width):
            px = min_x + x * dx
            py = max_y - y * dy
            pixel = Point(px,py,0)
            v = vector_from_to(eye_point,pixel)
            ray = Ray(eye_point,v)
            cl = cast_ray(ray,sphere_list,clr,Light,eye_point)
            print int(255 * cl.r),int(255 * cl.g),int(255 * cl.b)
