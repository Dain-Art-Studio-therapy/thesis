import cast
from data import *

def main():
   sphere1=Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1.0),Finish(.2,.4,.5,.05))
   sphere2=Sphere(Point(0.5,1.5,-3.0),.5,Color(1.0,0,0),Finish(.4,.4,.5,.05))
   sphere_list=[sphere1,sphere2]
   cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,Point(0.0,0.0,-14.0),sphere_list,Color(1.0,1.0,1.0),Light(Point(-100,100,-100),Color(1.5,1.5,1.5)))

if __name__=='__main__':
   main()
