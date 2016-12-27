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

        color_w_finish = FinishColor(sphere_color,sphere_finish)

        color_w_ambience = AmbienceColor(color_w_finish,ambience)
        
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
                color_w_light = LightColor(sphere_finish,sphere_color,light,p_e_dot)

                color_diffuse = DiffuseColor(color_w_ambience,color_w_light)

                if spec_intensity > 0:
                    roughness_value = sphere_finish.roughness
                    rough_powerTo = 1/roughness_value
                    raised_spec_intensity = spec_intensity**rough_powerTo
                    spec_mult = sphere_finish.specular * raised_spec_intensity

                    spec_product = SpecProduct(light,spec_mult)

                    color_spec = SpecColor(color_diffuse,spec_product)

                    return color_spec

                else:
                    return color_diffuse

        else:
            return color_w_ambience

    return whiteColor
        
def cast_all_rays(min_x, max_x, min_y, max_y, w, h, eye_pt, sph_lst, amb, lte):
    image_file = open("image.ppm",'w')

    image_file.write("P3\n")
    image_file.write(str(w) + " " + str(h) + "\n")
    image_file.write("255\n")
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
            image_file.write(str(pixel_r)+" "+str(pixel_g)+" "+str(pixel_b))
            image_file.write(" \n")

    image_file.close()

def checkMin(color_value):
    if color_value > 255:
        color_value = 255
        return color_value
    else:
        return color_value

def FinishColor(s_color,s_finish):
    finish_r = s_color.r*s_finish.ambient
    finish_g = s_color.g*s_finish.ambient
    finish_b = s_color.b*s_finish.ambient
    new_color = Color(finish_r, finish_g,finish_b)
    return new_color

def AmbienceColor(c_finish,amb):
    ambience_r = c_finish.r*amb.r
    ambience_g = c_finish.g*amb.g
    ambience_b = c_finish.b*amb.b
    new_color = Color(ambience_r,ambience_g,ambience_b)
    return new_color

def LightColor(s_finish,s_color,light,pe_dot):
    lightC_mult = s_finish.diffuse * pe_dot
    lightC_r = s_color.r * light.color.r * lightC_mult
    lightC_g = s_color.g * light.color.g * lightC_mult
    lightC_b = s_color.b * light.color.b * lightC_mult
    new_color = Color(lightC_r,lightC_g,lightC_b)
    return new_color

def DiffuseColor(c_amb,c_light):
    diffuse_r = c_amb.r+c_light.r
    diffuse_g = c_amb.g+c_light.g
    diffuse_b = c_amb.b+c_light.b
    new_color = Color(diffuse_r, diffuse_g, diffuse_b)
    return new_color

def SpecProduct(light,spec_mult):
    spec_product_r = (light.color.r * spec_mult)
    spec_product_g = (light.color.g * spec_mult)
    spec_product_b = (light.color.b * spec_mult)
    new_color = Color(spec_product_r,spec_product_g,spec_product_b)
    return new_color

def SpecColor(color_diffuse,spec_product):
    spec_r = color_diffuse.r + spec_product.r
    spec_g = color_diffuse.g + spec_product.g
    spec_b = color_diffuse.b + spec_product.b
    new_color = Color(spec_r,spec_g,spec_b)
    return new_color