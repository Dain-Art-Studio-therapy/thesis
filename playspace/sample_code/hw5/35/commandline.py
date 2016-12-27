# usage: python ray_caster.py <filename>
# [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]

from ray_caster import *

def parseargs(argv):
   if len(argv) <= 1:
      print "Give an file name"
      exit(1)
   else:
      eye_point = Point(0.0, 0.0, -14.0)
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      view = View(-10.0, 10.0, -7.5, 7.5, 1024, 768)
      ambient = Color(1.0, 1.0, 1.0)
      if "-eye" in argv:
         print "-eye found"
         eye = get_next_n_args("-eye", 3, argv)
         if eye is not None:
            eye_point = Point(eye[0], eye[1], eye[2])
      if "-view" in argv:
         print "-view found"
         av = get_next_n_args("-view", 6, argv)
         if av is not None:
            view = View(av[0], av[1], av[2], av[3], av[4], av[5])
      if "-light" in argv:
         print "-light found"
         al = get_next_n_args("-light", 6, argv)
         if al is not None:
            pt = Point(al[0], al[1], al[2])
            color = Color(al[3], al[4], al[5])
            light = Light(pt, color)
      if "-ambient" in argv:
         print "-ambient found"
         am = get_next_n_args("-ambient", 3, argv)
         if am is not None:
            ambient = Color(am[0], am[1], am[2])
      cast_all_rays_from_file(argv[1], eye_point, view, light, ambient)

def get_next_n_args(needle, n, args):
   amount = 0
   nextn = []
   found = False
   for arg in args:
      if found and n > amount:
         try:
            nextn.append(float(arg))
         except:
            print "Error in parsing", needle, ", check your arguments"
            return None
         amount += 1
      if arg == needle:
         found = True
   if len(nextn) != n:
      print "Incorrect amount of arguments for", needle
      return None
   return nextn



if __name__ == "__main__":
   parseargs(sys.argv)