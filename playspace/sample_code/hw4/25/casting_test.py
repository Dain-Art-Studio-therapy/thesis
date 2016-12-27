import data
import cast

print "P3"
print 1024, 768
print 255

points= [data.Point(1.0, 1.0, 0.0), data.Point(0.5, 1.5, -3.0), data.Point(0.0, 0.0, -14.0), data.Point(-100.0, 100.0, -100.0)]
radii= [2.0, 0.5]
colors= [data.Color(0.0, 0.0, 1.0), data.Color(1.0, 0.0, 0.0), data.Color(1.5, 1.5, 1.5)]
finish= [data.Finish(0.2, 0.4, 0.5, 0.05), data.Finish(0.4, 0.4, 0.5, 0.05)]
spheres= [data.Sphere(points[0], radii[0], colors[0], finish[0]), data.Sphere(points[1], radii[1], colors[1], finish[1])]
list= [spheres[0], spheres[1]]
light= data.Light(points[3], colors[2])
ambientcolor= data.Color(1.0, 1.0, 1.0)
cast.cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, points[2], list, ambientcolor, light)
