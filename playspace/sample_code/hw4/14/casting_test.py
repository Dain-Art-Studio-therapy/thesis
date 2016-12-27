#Contains Main Function and scene cast test
import data
import cast


width = 1024
height = 768
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
a_color = data.Color(1.0, 1.0, 1.0)
eye_point = data.Point(0.0, 0.0, -14.0)
point_light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5,
   1.5))
sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0, 0.0, 1.0),
   data.Finish(0.2, 0.4, 0.5, 0.05))
sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0.0, 0.0)
   , data.Finish(0.4, 0.4, 0.5, 0.05))
sphere_list = [sphere1, sphere2]
print"P3\n%d %d\n255" %(width, height)
cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
   sphere_list, a_color, point_light)



