import data
import vector_math
import collisions 
import cast

print "P3 \n", 1024, 768, "255" 


cast.cast_all_rays(-10, 10, -7.0, 7.5, 
1024, 768, 
data.Point(0.0,0.0,-14.0), [
data.Sphere(data.Point(1.0,1.0,0.0), 2.0, data.Color(0.0,0.0,1.0), data.Finish(0.2, 0.4)), 
data.Sphere(data.Point(0.5, 1.5,-3.0), 0.5, data.Color(1.0,0.0,0.0), data.Finish(0.4, 0.4))],
data.Color(1.0,1.0,1.0),
data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)))