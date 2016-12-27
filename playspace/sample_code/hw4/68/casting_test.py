print "P3"
print "20 20"
print "255"
import data
import cast
eye_point = data.Point(0.0, 0.0, -14.0)
p1 = data.Point(1.0, 1.0, 0.0)
p2 = data.Point(0.5, 1.5, -3.0)
sph = data.Sphere(p1, 2.0, data.Color(0, 0, 1.0), data.Finish(0.2))
sph2 = data.Sphere(p2, 0.5, data.Color(1.0, 0, 0), data.Finish(0.4))
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
sphere_list = [sph, sph2]
acolor = data.Color(1.0, 1.0, 1.0)
light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, acolor, light)
