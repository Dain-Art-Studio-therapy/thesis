import sys
import data
import vector_math
import cast
import collisions
import commandline


#The main function that runs the program
def caster(argv):
   user_input = commandline.command(argv)
   o = open_file(user_input)

   #Data for the cast_all_rays function
   user_input = commandline.command(argv)
   eye_point = user_input[0]
   min_x = user_input[1]
   max_x = user_input[2]
   min_y = user_input[3]
   max_y = user_input[4]
   width = user_input[6]
   height = user_input[5]
   color = user_input[8]
   light = user_input[7]
   new_list = process_file(o)          
   x = open('image.ppm','r+b')
   ppm = "P3\n1024 768\n255\n" 
   x.write(ppm)
   o.close()

   #Attempt to use the data!
   try:
      image = cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,new_list,color,light)
      x.write(image)
      x.close()
   except:
      print new_list
      x.close()


#Attempts to open the file designated by the user
def open_file(user_input):
   try:
      return open(user_input[9],'rb')
   except IOError as e:
      print >>sys.stderr, '{0}: {1}'.format(user_input[9], e.strerror)
      exit(1)


#Takes the input file and gives back a list of spheres if possible, else it will return a list of errors
def process_file(o):
   sphere_list = []
   for line in o:
      nums = line.split()
      l = list(nums)
      try:
         p = data.Point(float(l[0]), float(l[1]), float(l[2]))
         r = (float(l[3]))
         c = data.Color(float(l[4]),float(l[5]), float(l[6]))
         f = data.Finish(float(l[7]),float(l[8]),float(l[9]),float(l[10]))
         sphere = data.Sphere(p,r,c,f) 
         sphere_list.append(sphere)
      except:
         error = "MALFORMED SPHERE IN FILE:", line
         sphere_list.append(error) 
   return sphere_list 

   

if __name__ == '__main__':
   caster(sys.argv)

