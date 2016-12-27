import cast
import data

def main():
   p = data.Point(0.0, 0.0, -14.0)

   s1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.05))
   s2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0, 0), data.Finish(0.4, 0.4, 0.5, 0.05))
   l1 = [s1, s2]

   c = data.Color(1.0, 1.0, 1.0)
 
   light_pt = data.Point(-100.0, 100.0, -100.0)
   light_color = data.Color(1.5, 1.5, 1.5)
   light = data.Light(light_pt, light_color)

   cast.cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, p, l1, c, light)

if __name__ == '__main__':
   main() 
