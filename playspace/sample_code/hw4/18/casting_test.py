from castCP import *
from data import *

eye = Point(0.0, 0.0, -14.0)
sphereList = [Sphere(Point(1.0,1.0,0.0), 2, Color(0,0,1), Finish(.2,.4,.5,.05))
   , Sphere(Point(0.5, 1.5, -3.0), .5, Color(1,0,0), Finish(.4,.4,.5,.05))]
minX = -10 
maxX = 10
minY = -7.5
maxY = 7.5
width = 1024
height = 768
ambient = Color(1,1,1)
sceneLight = Light(Point(-100.0, 100.0, -100.0), Color(1.5,1.5,1.5))


cast_all_rays(minX, maxX, minY, maxY, width, height, eye, sphereList, ambient, 
   sceneLight)

