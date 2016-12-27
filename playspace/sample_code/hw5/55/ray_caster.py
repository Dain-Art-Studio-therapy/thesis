from cast import *
import commandline as cmd
import sys

def open_file(name, mode):
   try: 
      return open(name[1], mode)
   except:
      print "Error: missing file to read"
      sys.exit()

def get_spherelist_from_file(argv):
   spherefile= open_file(argv, 'r')
   linenum= 0
   result= []
   for line in spherefile:
      linenum+=1
      linelist= line.split()
      #print linelist
      if linelist == []:
         print "Error: No Values in Line "+str(linenum)+"... skipping"
         continue
      if len(linelist) !=11:
         print "Error: Incorrect Num of Values in Line "+str(linenum)+"... skipping"
         continue

      try:
         x= float(linelist[0])
         y=float(linelist[1])
         z=float(linelist[2])
         radius=float(linelist[3])
         r=float(linelist[4])
         g=float(linelist[5])
         b=float(linelist[6])
         ambient=float(linelist[7])
         diffuse=float(linelist[8])
         specular=float(linelist[9])
         roughness=float(linelist[10])
      except:
         print "Error: Malformed Sphere on Line "+str(linenum)+"... skipping"
      try:
         result.append(Sphere(Point(x,y,z), radius, Color(r,g,b), Finish(ambient, diffuse, specular, roughness)))
      except:
         print "Error: Malformed Sphere on Line "+str(linenum)+"... skipping"
      
   spherefile.close 
   return result
   
#test4= get_spherelist_from_file([0,0,'crapdoc.txt'])
#print test4

def main(argv):
   arg_list= cmd.commands(argv)
   view= arg_list[0]
   eye_point= arg_list[1]
   sphere_list= get_spherelist_from_file(argv)
   ambient_light=arg_list[2]
   lightsource= arg_list[3]
   cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5], eye_point, sphere_list, ambient_light, lightsource)

   
if __name__=='__main__':
   main(sys.argv)