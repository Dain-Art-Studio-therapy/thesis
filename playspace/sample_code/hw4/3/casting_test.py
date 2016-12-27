import cast
import data

eye_point = data.Point(0.0, 0.0, -14.0)
b = data.Color(0.0, 0.0, 1.0)
r = data.Color(1.0, 0.0, 0.0)
finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
finish2 = data.Finish(0.4, 0.4, 0.5, 0.05)
sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, b, finish1)
sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, r, finish2)
sphere_list = [sphere1, sphere2]
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
ambient = data.Color(1.0, 1.0, 1.0)
lightPoint = data.Point(-100.0, 100.0, -100.0)
lightColor = data.Color(1.5, 1.5, 1.5)
light = data.Light(lightPoint, lightColor)
cast.cast_all_rays(min_x, max_x, min_y, max_y,\
				   width, height, eye_point, sphere_list, ambient, light)