import unittest
import cast
import data

print 'P3'
print '1024 768'
print '255'
print cast.cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768,
       data.Point(0.0, 0.0, -14.0), [data.Sphere(data.Point(
       1.0, 1.0, 0.0), float(2.0), data.Color(0, 0, 255), data.Finish(0.2, 0.4, 0.5, 0.05)),
       data.Sphere(data.Point(0.5, 1.5, -3.0), float(0.5), 
       data.Color(255, 0, 0), data.Finish(0.4, 0.4, 0.5, 0.05))], data.Color(1.0, 1.0, 1.0), data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)))
