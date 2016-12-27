import sys
import data
import commandline
import cast

def main(argv):
   try:
      file = open(argv[1], 'rb')
   except:
       if(len(argv) < 2):
          print sys.exit('usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]')
       else:
          print sys.exit('File does not exist or cannot be opened')
   list = []
   spherelist= []
   for line in file:
      list = line.split()
      if (len(list) != 11):
         print 'malformed sphere on'
         print line
      for e in line:
         if (e.isalpha() == True):
            print 'malformed sphere on'
            print line
            break
      else:
         x1 = float(list[0])
         y1 = float(list[1])
         z1 = float(list[2])
         radius = float(list[3])
         r1 = float(list[4])
         g1 = float(list[5])
         b1 = float(list[6])
         ambient = float(list[7])
         diffuse = float(list[8])
         specular = float(list[9])
         roughness = float(list[10])
         sphere = data.Sphere(data.Point(x1, y1, z1), radius, data.Color(r1, g1, b1), data.Finish(ambient, diffuse, specular, roughness))
         spherelist.append(sphere)
   eye_pt = commandline.find_eye(argv)
   view_list = commandline.find_view(argv)
   light = commandline.find_light(argv)
   ambient = commandline.find_ambient(argv)
   cast.cast_all_rays(float(view_list[0]), float(view_list[1]), float(view_list[2]), float(view_list[3]), int(view_list[4]), int(view_list[5]), eye_pt, spherelist, ambient, light)
   

if __name__ == "__main__":
   main(sys.argv)
