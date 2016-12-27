from data import *
from vector_math import *
from collisions import *

def cast_ray(ray,sphere_list,ambience,light,eye_point):
    cast_list =  find_intersection_points(sphere_list,ray)
    whiteColor = Color(1.0,1.0,1.0)

    if cast_list != []:

        dist_list = [(i[1].x**2+i[1].y**2)**0.5 for i in cast_list]
        sphere_index = dist_list.index(min(dist_list))
        sphere_color = cast_list[dist_list.index(min(dist_list))][0].color
        sphere_center = cast_list[dist_list.index(min(dist_list))][0].center
        sphere_intersection_pt = cast_list[dist_list.index(min(dist_list))][1]
        sphere_finish = cast_list[dist_list.index(min(dist_list))][0].finish

        finish_r = sphere_color.r*sphere_finish.ambient
        finish_g = sphere_color.g*sphere_finish.ambient
        finish_b = sphere_color.b*sphere_finish.ambient
        color_w_finish = Color(finish_r, finish_g,finish_b)

        ambience_r = color_w_finish.r*ambience.r
        ambience_g = color_w_finish.g*ambience.g
        ambience_b = color_w_finish.b*ambience.b
        color_w_ambience = Color(ambience_r,ambience_g,ambience_b)
        
        N_vect = vector_from_to(sphere_center,sphere_intersection_pt)
        N = normalize_vector(N_vect)
        p_e = translate_point(sphere_intersection_pt,scale_vector(N,0.01))
        l_dir = normalize_vector(vector_from_to(p_e,light.point))
        p_e_dot = dot_vector(N,l_dir)

        light_pe_ray = Ray(p_e,l_dir)
        light_intersection = find_intersection_points(sphere_list,light_pe_ray)

        l_dot_N = dot_vector(l_dir,N)

        refl_mult = (2 * l_dot_N)
        refl_scale = scale_vector(N,refl_mult)
        reflection_vect = difference_vector(l_dir, refl_scale)

        eye_pe_vector = difference_point(p_e,eye_point)
        v_dir = normalize_vector(eye_pe_vector)
        spec_intensity = dot_vector(reflection_vect,v_dir)

        if p_e_dot > 0:

            if (light_intersection != []):
                return color_w_ambience

            else: 
                lightC_mult = sphere_finish.diffuse * p_e_dot
                lightC_r = sphere_color.r * light.color.r * lightC_mult
                lightC_g = sphere_color.g * light.color.g * lightC_mult
                lightC_b = sphere_color.b * light.color.b * lightC_mult

                color_w_light = Color(lightC_r,lightC_g,lightC_b)

                diffuse_r = color_w_ambience.r+color_w_light.r
                diffuse_g = color_w_ambience.g+color_w_light.g
                diffuse_b = color_w_ambience.b+color_w_light.b

                color_diffuse = Color(diffuse_r, diffuse_g, diffuse_b)

                if spec_intensity > 0:
                    roughness_value = sphere_finish.roughness
                    rough_powerTo = 1/roughness_value
                    raised_spec_intensity = spec_intensity**rough_powerTo

                    spec_mult = sphere_finish.specular * raised_spec_intensity
                    spec_product_r = (light.color.r * spec_mult)
                    spec_product_g = (light.color.g * spec_mult)
                    spec_product_b = (light.color.b * spec_mult)

                    spec_r = color_diffuse.r + spec_product_r
                    spec_g = color_diffuse.g + spec_product_g
                    spec_b = color_diffuse.b + spec_product_b

                    color_spec = Color(spec_r,spec_g,spec_b)

                    return color_spec

                else:
                    return color_diffuse

        else:
            return color_w_ambience

    return whiteColor
        
def cast_all_rays(min_x, max_x, min_y, max_y, w, h, eye_pt, sph_lst, amb, lte):
    print "P3"
    print w, h
    print "255"
    deltaX = (max_x - min_x)/float(w)
    deltaY = (max_y - min_y)/float(h)
    for y in range(h):
        for x in range(w):
            x_val = min_x + (x*deltaX)
            y_val = max_y - (y*deltaY)
            dir_pt = Point(x_val,y_val,0)
            dir = vector_from_to(eye_pt,dir_pt)
            eye_ray = Ray(eye_pt,dir)
            returning_pixel = cast_ray(eye_ray,sph_lst,amb,lte,eye_pt)

            pixel_r = checkMin(int(returning_pixel.r*255))
            pixel_g = checkMin(int(returning_pixel.g*255))
            pixel_b = checkMin(int(returning_pixel.b*255))
            print str(pixel_r)+" "+str(pixel_g)+" "+str(pixel_b)

def checkMin(color_value):
    if color_value > 255:
        color_value = 255
        return color_value
    else:
        return color_value




