# test file for running specific cases that test the raycast system
# may cause strange things to happen, use with caution

import cast
import data

def main():
    BLUE = data.Color(0.0,0.0,1.0)
    RED = data.Color(1.0,0.0,0.0)
    WHITE = data.Color(1.0,1.0,1.0)
    lightpt = data.Point(-100.0,100.0,-100.0)
    lcol = data.Color(1.5,1.5,1.5)
    light = data.Light(lightpt,lcol)
    s1 = data.Sphere(data.Point(1.0,1.0,0.0),2,BLUE,data.Finish(0.2,0.4,0.5,0.05))
    s2 = data.Sphere(data.Point(0.5,1.5,-3.0),.5,RED,data.Finish(0.4,0.4,0.5,0.05))
    slist = [s1,s2]
    eye = data.Point(0.0,0.0,-14.0)
    cast.cast_all_rays(-10,10,-7.5,7.5,1024,768,eye,slist,WHITE,light)

    
if __name__ == "__main__":
    main()

    
