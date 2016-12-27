import data
import cast 


def rays():
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)) 
    ambient_color = data.Color(1.0, 1.0, 1.0)
    eye_point = data.Point(0.0, 0.0, -14.0) 
    sphere = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.05))
    sphere1 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05))
    sphere_list = [sphere, sphere1] 
    print "P3"
    print 1024, 768 
    print 255 
    cast.cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, eye_point, sphere_list, ambient_color, light)



if __name__== '__main__':
    rays()
