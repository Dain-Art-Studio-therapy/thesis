import cast
import data

def main():
    print 'P3'
    print 1024, 768
    print 255
    eye = data.Point(0.0,0.0,-14.0)
    s1 = data.Sphere(data.Point(1.0,1.0,0.0), 2.0, data.Color(0,0,1), data.Finish(0.2, 0.4, 0.5, 0.05))
    s2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1,0,0), data.Finish(0.4, 0.4, 0.5, 0.05))
    light_pt = data.Point(-100.0,100.0,-100.0)
    light_color = data.Color(1.5,1.5,1.5)
    cast.cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768, eye, [s1,s2], data.Color(1.0,1.0,1.0), data.Light(light_pt, light_color))

if __name__ =='__main__':main()
