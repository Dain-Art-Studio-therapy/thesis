print 'P3'
print '1024 768'
print '255'

import cast
import data

# cast_all_rays(min_x, max_x, min_y, max_y, width, height,\
 # eye_point, sphere_list, color, light):

# cast_ray(ray, sphere_list, color, light):
  # sphere(center, rad, color, finish)

larger_sphere = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, \
	data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.05))

smaller_sphere = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5,\
	data.Color(1.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05))   

sphere_list = [larger_sphere, smaller_sphere]

cast.cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768,\
	data.Point(0.0, 0.0, -14.0), sphere_list, data.Color(1.0, 1.0, 1.0),\
	   data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)))
