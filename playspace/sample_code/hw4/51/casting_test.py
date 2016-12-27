import cast
import data
print 'P3'
print '1024 768'
print '255'
eye = data.Point(0.0,0.0,-14.0)
s1 = data.Sphere(data.Point(1.0,1.0,0.0),2.0,data.Color(0.0,0.0,1.0),data.Finish(.2,.4,.5,.05))
s2 = data.Sphere(data.Point(.5,1.5,-3.0),.5,data.Color(1.0,0.0,0.0),data.Finish(.4,.4,.5,.05))
S = [s1,s2]
l = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))

cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,eye,S,data.Color(1.0,1.0,1.0),l) 
