from collisions import *
import vector_math
import data
import math
import sys


def distance(point1,point2):
    return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)



def nearest_sphere(sphere_list,ray):
    #sphere_list = list of spheres and corresponding intersection points
    smallest = 0
    for i in range(1,len(sphere_list)):
        d = distance(ray.pt,sphere_list[i][1])
        if d < distance(ray.pt,sphere_list[smallest][1]):
            smallest = i
    return smallest


#no intersection = white,
#nearest sphere = red,
#other spheres = blue



def cast_ray(ray,sphere_list,color,light,point):
        n = find_intersection_points(sphere_list,ray)
        # n returns a list with spheres and corresponding intersection points
        if n == []:
            return data.Color(1.0,1.0,1.0)

        l = nearest_sphere(n,ray) #returns index of smallest sphere
        sphere_finish = n[l][0].finish
        sphere_color = n[l][0].color

        #sphere color x finish ambiance
        r_sph_x_ambient = sphere_color.r * sphere_finish.ambient
        g_sph_x_ambient = sphere_color.g * sphere_finish.ambient
        b_sph_x_ambient = sphere_color.b * sphere_finish.ambient

        finish_times_color = data.Color(r_sph_x_ambient,g_sph_x_ambient,b_sph_x_ambient)

        #finish_times_color x color
        r_color_times_finish = finish_times_color.r * color.r
        g_color_times_finish = finish_times_color.g * color.g
        b_color_times_finish = finish_times_color.b * color.b

        color_times_ambiance = data.Color(r_color_times_finish, g_color_times_finish, b_color_times_finish)



        sphere_normal = sphere_normal_at_point(n[l][0],n[l][1])
        shorter_vector = vector_math.scale_vector(sphere_normal,0.01)
        p3 = vector_math.translate_point(n[l][1],shorter_vector) #returns point
        point_diff = vector_math.difference_point(light.point,p3) #returns vector
        Ldir = normalize_vector(point_diff)
        visible = vector_math.dot_vector(sphere_normal,Ldir)
        ray1 = data.Ray(p3, Ldir)
        list_2 = find_intersection_points(sphere_list,ray1)

        if visible > 0 and list_2 == []:

            #dot product times light color
            dot_x_ltcolor_r = visible * light.color.r
            dot_x_ltcolor_g = visible * light.color.g
            dot_x_ltcolor_b = visible * light.color.b

            dot_times_light_color = data.Color(dot_x_ltcolor_r,dot_x_ltcolor_g,dot_x_ltcolor_b)

            #new light color times sphere color
            r_light_x_sphere = dot_times_light_color.r * sphere_color.r
            g_light_x_sphere = dot_times_light_color.g * sphere_color.g
            b_light_x_sphere = dot_times_light_color.b * sphere_color.b

            light_color_times_sphere_color = data.Color(r_light_x_sphere, g_light_x_sphere, b_light_x_sphere)

            #diffuse times sphere color
            sphere_diffuse =  n[l][0].finish.diffuse
            r_sphere_x_diff = light_color_times_sphere_color.r * sphere_diffuse
            g_sphere_x_diff = light_color_times_sphere_color.g * sphere_diffuse
            b_sphere_x_diff = light_color_times_sphere_color.b * n[l][0].finish.diffuse

            diffuse_times_sphere_color = data.Color(r_sphere_x_diff, g_sphere_x_diff, b_sphere_x_diff)

            #ambiance plus diffuse
            add_r = color_times_ambiance.r + diffuse_times_sphere_color.r
            add_g = color_times_ambiance.g + diffuse_times_sphere_color.g
            add_b = color_times_ambiance.b + diffuse_times_sphere_color.b

            ambiance_and_diffuse = data.Color(add_r, add_g, add_b)

            #part 5
            scalar = 2 * visible
            vector_1 = vector_math.scale_vector(sphere_normal, scalar)
            reflection_vector = vector_math.difference_vector(vector_1, Ldir)
            point_diff_2 = vector_math.difference_point(point, p3)
            Vdir = vector_math.normalize_vector(point_diff_2)
            specular_intensity = vector_math.dot_vector(Vdir, reflection_vector)


            if specular_intensity > 0:

                #light color times sphere's specular
                sphere_specular =  n[l][0].finish.specular
                r_ltcolor_x_finish = light.color.r * sphere_specular
                g_ltcolor_x_finish = light.color.g * sphere_specular
                b_ltcolor_x_finish = light.color.b * sphere_specular

                color_times_specular = data.Color(r_ltcolor_x_finish, g_ltcolor_x_finish, b_ltcolor_x_finish)

                roughness_divided = 1/n[l][0].finish.roughness
                raised_specular = specular_intensity ** roughness_divided

                #specular times intensity
                r_color_x_spec = color_times_specular.r * raised_specular
                g_color_x_spec = color_times_specular.g * raised_specular
                b_color_x_spec = color_times_specular.b * raised_specular

                specular_times_intensity = data.Color(r_color_x_spec, g_color_x_spec, b_color_x_spec)

                #specular times intensity PLUS ambiance times diffuse
                r_spec_add = specular_times_intensity.r + ambiance_and_diffuse.r
                g_spec_add = specular_times_intensity.g + ambiance_and_diffuse.g
                b_spec_add = specular_times_intensity.b + ambiance_and_diffuse.b

                spec_and_diffuse = data.Color(r_spec_add, g_spec_add, b_spec_add)

                return spec_and_diffuse

            else:
                return ambiance_and_diffuse

        else:
            return color_times_ambiance



def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light):
    print 'P3'
    print width, height
    print 255

    #finds how many pixels in width and height
    dx = (max_x - min_x)/float(width)
    dy = (max_y - min_y)/float(height)
    for y in (range(height)):
        #for each y in height of image
        for x in(range(width)):
            image_point = data.Point(min_x + x * dx,max_y - y * dy,0)
            vector = vector_math.vector_from_to(eye_point,image_point)
            ray1 = data.Ray(eye_point,vector)
            col = cast_ray(ray1,sphere_list,color,light,eye_point)
            col_r = int(col.r * 255)
            col_g = int(col.g * 255)
            col_b = int(col.b * 255)

            if col_r > 255:
                col_r = 255

            if col_g > 255:
                col_g = 255

            if col_b > 255:
                col_b = 255



            print col_r,col_g,col_b




