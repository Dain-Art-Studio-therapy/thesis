import sys
from commandline import read
import commandline
import data
from cast import cast_all_rays
from sys import argv


def main(argv):

   try:
        with open('image.ppm', 'w') as output:
             writeFile(output)
   except IndexError:
       print >> sys.stderr, 'parameter not received'
       exit()
   except IOError:
       print >> sys.stderr, 'file could not be opened'
       exit()
   except AttributeError:
       print >> sys.stderr, 'completed'
       exit()
   except TypeError:
       print >> sys.stderr, 'completed'
       exit()



def writeFile(output):
         try:
            spheres = read(argv)[0]

            min_x  = read(argv)[1][0]
            max_x  = read(argv)[1][1]
            min_y  = read(argv)[1][2]
            max_y  = read(argv)[1][3]
            height = read(argv)[1][4]
            width  = read(argv)[1][5]
            eye_point = read(argv)[1][6]
            color = read(argv)[1][7]

            light = read(argv)[1][8]

            cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, spheres, color, light, output)
         except Exception as e:
               print repr(e)

if __name__ == '__main__':
    main(sys.argv)