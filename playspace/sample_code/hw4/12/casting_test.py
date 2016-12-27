from cast import *
from data import *

def main():
        eyePoint = Point(0.0,0.0,-14.0)
        finish1 = 0.2
        diff1 = 0.4
        finish2 = 0.4
        diff2 = 0.4
        specular = 0.5
        roughness = 0.05
        sph = Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1.0),Finish(finish1,diff1,specular,roughness))
	sph1 = Sphere(Point(0.5,1.5,-3.0),0.5,Color(1.0,0,0),Finish(finish2,diff2,specular,roughness))
        sphList = [sph,sph1]
	max_x = 10
	max_y = 7.5
	min_x = -10
	min_y = -7.5
        lightPoint = Point(-100.0,100.0,-100.0)
        lightColor = Color(1.5,1.5,1.5)
        light = Light(lightPoint,lightColor)
        ambientColor = Color(1.0,1.0,1.0)
        cast_all_rays(min_x,max_x,min_y,max_y,1024,768,eyePoint,sphList,ambientColor,light)



if __name__ == '__main__':
        main()
