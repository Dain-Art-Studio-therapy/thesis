import data
import cast


print 'P3'
print 1024, 768
print 255, '\n'


sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, 
	                   data.Color(0.0, 0.0, 1.0),
	                   data.Finish(.2, .4, 0.5, 0.05)),
	       data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, 
		           data.Color(1.0, 0.0, 0.0),
		           data.Finish(.4, .4, 0.5, 0.05))]

cast.cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768, data.Point(0.0, 0.0, -14.0),
		   sphere_list, data.Color(1.0, 1.0, 1.0), 
		   data.Light(data.Point(-100.0, 100.0, -100.0), 
			   data.Color(1.5, 1.5, 1.5)))

