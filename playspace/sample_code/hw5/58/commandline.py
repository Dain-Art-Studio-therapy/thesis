import sys
import data

def open_file(name):
   try:
      return open(name, 'rb')
   except IOError as e:
      print >> sys.stderr, '{1}'.format(name, e.strerror)
      exit(1)

def main(argv):
   spheres = []
   with open_file(argv[1]) as f:
      for line in f:
         sph = line.split(' ')
         if len(sph) == 11:
            try:
               spheres.append(data.Sphere(data.Point(float(sph[0]),
                      float(sph[1]), float(sph[2])), float(sph[3]), 
                      data.Color(float(sph[4]), float(sph[5]), 
                      float(sph[6])), data.Finish(float(sph[7]),
                      float(sph[8]), float(sph[9]), 
                      float(sph[10]))))
            except:
               pass  

   return spheres
         
if __name__ == '__main__':
   main(sys.argv)

