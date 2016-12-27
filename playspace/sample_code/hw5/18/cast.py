from collisions import *
from vector_math import *


def color_change(color):
    r = color.r * 255
    g = color.g * 255
    b = color.b * 255
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    return Color(int(r), int(g), int(b))


def color_with_ambient(ambient_color, sphere):
    r = sphere.color.r * sphere.finish.ambient * ambient_color.r
    g = sphere.color.g * sphere.finish.ambient * ambient_color.g
    b = sphere.color.b * sphere.finish.ambient * ambient_color.b
    return Color(r, g, b)


def color_with_diffuse(visibility, light, sphere):
    r = sphere.color.r * sphere.finish.diffuse * visibility * light.color.r
    g = sphere.color.g * sphere.finish.diffuse * visibility * light.color.g
    b = sphere.color.b * sphere.finish.diffuse * visibility * light.color.b
    return Color(r, g, b)


def color_with_intensity(light, sphere, intensity):
    rgh = 1 / sphere.finish.roughness
    r = light.color.r * sphere.finish.specular * (intensity ** rgh)
    g = light.color.g * sphere.finish.specular * (intensity ** rgh)
    b = light.color.b * sphere.finish.specular * (intensity ** rgh)
    return Color(r, g, b)


def ambient_and_diffuse(color_ambient, color_diffuse):
    r = color_ambient.r + color_diffuse.r
    g = color_ambient.g + color_diffuse.g
    b = color_ambient.b + color_diffuse.b
    return Color(r, g, b)


def ambient_diffuse_and_intensity(col_amb, col_diff, col_int):
    r = col_amb.r + col_diff.r + col_int.r
    g = col_amb.g + col_diff.g + col_int.g
    b = col_amb.b + col_diff.b + col_int.b
    return Color(r, g, b)


def shift_intersection_point(point, normal_vector):
    scaled_vector = scale_vector(normal_vector, 0.01)
    shifted_point = translate_point(point, scaled_vector)
    return shifted_point


def cast_ray(ray, sphere_list, ambient_color, light, eye_position):
    a = find_intersection_points(sphere_list, ray)
    # [(sp, pt)]
    if a:
        min_dis_ind = 0
        min_v = vector_from_to(ray.pt, a[min_dis_ind][1])
        for i in range(len(a)):
            v = vector_from_to(ray.pt, a[i][1])
            if length_vector(v) < length_vector(min_v):
                min_dis_ind = i
                min_v = vector_from_to(ray.pt, a[i][1])

        closest_sphr = a[min_dis_ind][0]
        # part 3 data
        N = sphere_normal_at_point(closest_sphr, a[min_dis_ind][1])
        P_e = shift_intersection_point(a[min_dis_ind][1], N)
        L_dir = normalize_vector(vector_from_to(P_e, light.pt))
        contribute = True
        visibility = dot_vector(N, L_dir)
        # part 4 data
        scale_value = 2 * visibility
        reflection_vector = difference_vector(L_dir, scale_vector(N, scale_value))
        V_dir = normalize_vector(vector_from_to(eye_position, P_e))
        specular_intensity = dot_vector(V_dir, reflection_vector)

        if visibility > 0:
            b = find_intersection_points(sphere_list, Ray(P_e, L_dir))
            if b:
                P_L_vector = vector_from_to(P_e, light.pt)
                for i in range(len(b)):
                    vctr = vector_from_to(P_e, b[i][1])
                    if length_vector(vctr) < length_vector(P_L_vector):
                        contribute = False
            else:
                contribute = True
        else:
            contribute = False
        amb_col = color_with_ambient(ambient_color, closest_sphr)
        diff_col = color_with_diffuse(visibility, light, closest_sphr)
        int_col = color_with_intensity(light, closest_sphr, specular_intensity)

        if contribute and specular_intensity > 0:
            return ambient_diffuse_and_intensity(amb_col, diff_col, int_col)
        elif contribute:
            return ambient_and_diffuse(amb_col, diff_col)
        else:
            return amb_col
    else:
        return Color(1.0, 1.0, 1.0)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
                  eye_point, sphere_list, ambient_color, light, file_name):
    print >> file_name, "P3"
    print >> file_name, width, height
    print >> file_name, 255


    dx = (max_x - min_x) / float(width)
    dy = (max_y - min_y) / float(height)

    x_ = min_x
    y_ = max_y
    for y in range(height):
        for x in range(width):
            pt = Point(x_, y_, 0)
            dir = vector_from_to(eye_point, pt)
            r = Ray(eye_point, dir)
            hit = cast_ray(r, sphere_list, ambient_color, light, eye_point)
            x_ += dx

            if hit == Color(1.0, 1.0, 1.0):
                a = color_change(hit)
                print >> file_name, a.r, a.g, a.b
            else:
                b = color_change(hit)
                print >> file_name, b.r, b.g, b.b
        x_ = min_x
        y_ -= dy
