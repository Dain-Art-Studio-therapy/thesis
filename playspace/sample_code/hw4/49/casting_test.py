from cast import *

def main():
   cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768, Point(0, 0, -14), 
                 [Sphere(Point(1,1,0), 2, Color(0, 0, 1), Finish(0.2, 0.4, 0.5, 0.05)), 
                 Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1, 0, 0), Finish(0.4, 0.4, 0.5, 0.05))], 
                 Color(1, 1, 1), Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5)))
   # cast_all_rays(0.05859357, 0.05859357, 0.05859357, 0.05859357, 20, 20, Point(0, 0, -14), 
                   #[Sphere(Point(1,1,0), 2, Color(0, 0, 1), Finish(0.2, 0.4, 0.5, 0.05)), 
                   #Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1, 0, 0), 
                   #Finish(0.4, 0.4, 0.5, 0.05))], Color(1, 1, 1), 
                   #Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5)))

if __name__ == "__main__":
   main()
