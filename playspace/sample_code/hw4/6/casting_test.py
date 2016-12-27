import cast 
import data
import castcopy



eye_point = data.Point(0.0,0.0,-14.0)
S1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.5))
S2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0,0.0,0.0),data.Finish(0.4,0.4,0.5,0.5))
sphere_list = [S1,S2]
min_x = -10.0
max_x = 10.0
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
ambient_light = data.Color(1.0,1.0,1.0)
light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))
castcopy.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient_light,light)
