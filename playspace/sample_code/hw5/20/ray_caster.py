import commandline
import cast
import sys
from data import *
def main(argv):
   with open('image.ppm','w') as f:
      #d=commandline.read_arguments(argv)
      #print >> f,cast.cast_all_rays(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9])
      sphere1=Sphere(Point(1.0,1.0,0.0),2.0,Color(1,0,1.0),Finish(.2,.4,.5,.05))
      sphere2=Sphere(Point(8,-10,110),100,Color(.2,0.2,0.6),Finish(.4,.8,0,0.05))
      sphere_list=[sphere1,sphere2]
      print >> f,cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,Point(0.0,0.0,-14.0),sphere_list,Color(1.0,1.0,1.0),Light(Point(-100,100,-100),Color(1.5,1.5,1.5)))

if __name__=='__main__':
   main(sys.argv)
