import collisions
import data
import vector_math
import cast

eye = data.Point(0.0,0.0,-14.0)
point1 = data.Point(1.0,1.0,0.0)
point2 = data.Point(0.5,1.5,-3.0)
red = data.Color(255,0,0)
blue = data.Color(0,0,255)
finish1 = data.Finish(.2,.4)
finish2 = data.Finish(.4,.4)
sphere1 = data.Sphere(point1, 2.0,blue,finish1)
sphere2 = data.Sphere(point2, 0.5,red,finish2)
sphere_list = [sphere1, sphere2]
ambient = data.Color(1,1,1)
light_point = data.Point(-100.0,100.0,-100.0)
light_color = data.Color(1.5,1.5,1.5)
light = data.Light(light_point,light_color)
cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,eye,sphere_list,ambient,light)



