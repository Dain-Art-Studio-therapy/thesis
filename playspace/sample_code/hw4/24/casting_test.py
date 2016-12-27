import cast
import collisions
import vector_math
import data
import utility


mode = 'normal' # debug or normal

eye_point = data.Point(0, 0, -14)
sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.05))
sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0, 0), data.Finish(0.4, 0.4, 0.5, 0.05))
sphere_list = [sphere1, sphere2]
ambient_color = data.Color(1., 1., 1.)
light = data.Light(data.Point(-100, 100, -100), data.Color(1.5, 1.5, 1.5))
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 1024
height = 768

# debug values
min_x_d = 0.05859357
max_x_d = 0.44921857
min_y_d = 2.03125
max_y_d = 2.421875
width_d = 20
height_d = 20





if mode == 'debug':
   cast.cast_all_rays(min_x_d, max_x_d, min_y_d, max_y_d, width_d, height_d,
      eye_point, sphere_list, ambient_color, light)
else:
   cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
      sphere_list, ambient_color, light)
