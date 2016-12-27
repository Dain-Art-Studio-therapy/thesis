import collisions
import vector_math
import data
import math


def distance(point, ray):
    d = math.sqrt((point.x - ray.pt.x) ** 2 + (point.y - ray.pt.y) ** 2 + (point.z - ray.pt.z) ** 2)
    return d


def cast_ray(ray, sphere_list, acolor, light):
    sphere_color = data.Color(1.0, 1.0, 1.0)
    index = 0
    d = []
    nlist = collisions.find_intersection_point(sphere_list, ray)
    if nlist:
        for sp in nlist:
            # sp[0] = sphere  sp[1] = intersection point
            d.append(distance(sp[1], ray))
            for a in d:
                if a == min(d):
                    index = d.index(a)
                    sphere_color = sphere_list[index].color
                    r = sphere_color.r
                    g = sphere_color.g
                    b = sphere_color.b
                    f = sphere_list[index].finish
                    l = light.color
                    int_pt = collisions.sphere_intersection_points(ray, sphere_list[index])
                    sp_norm = collisions.sphere_normal_at_point(sphere_list[index], int_pt)
                    pe = vector_math.translate_point(int_pt, sp_norm)
                    dif = vector_math.difference_point(pe, light.pt)
                    ldif = vector_math.normalize_vector(dif)
                    dot_prod = vector_math.dot_vector(ldif, sp_norm)
                    ray2 = data.Ray(pe, dif)
                    if collisions.find_intersection_point(sphere_list, ray2):
                        red = acolor.r * r * f.ambient
                        grn = acolor.g * g * f.ambient
                        blu = acolor.b * b * f.ambient
                        return data.Color(red, grn, blu)
                    else:
                        red = acolor.r * r * f.ambient * dot_prod * l.r * f.diffuse
                        grn = acolor.g * g * f.ambient * dot_prod * l.g * f.diffuse
                        blu = acolor.b * b * f.ambient * dot_prod * l.b * f.diffuse
                        return data.Color(red, grn, blu)

    else:
        return sphere_color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, acolor, light):
    dx = (max_x - min_x) / float(width)
    dy = (max_y - min_y) / float(height)
    # vary x before y = go through y in first for loop then the x in second for loop
    for i in range(height):
        for j in range(width):
            y = max_y - i * dy
            x = min_x + j * dx
            v = vector_math.difference_point(data.Point(x, y, 0), eye_point)
            r = data.Ray(eye_point, v)
            cr = cast_ray(r, sphere_list, acolor, light)
            red = int(cr.r * 255)
            g = int(cr.g * 255)
            b = int(cr.b * 255)
            print red, g, b
