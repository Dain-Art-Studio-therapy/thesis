import data
import vector_math
import cast 
import collisions 

from sys import * 


def command():
   if len(argv) < 2: 
      print "not enough input parameters" 
      exit()

   else:    
      try: 
         f = open(argv[1], 'r')
         newf = open(argv[2], 'w')
         
         contents_list = f.read()

      except: 
         print "file does not exist" 
         exit()
      
   f.close() 
   
   sphere_list = []
   for a in range(len(contents_list)): 
      sphere_list.append(data.Sphere(
                              data.Point(float(contents_list[0]), float(contents_list[1]), float(contents_list[2])),
                                 float(contents_list[3]), 
                              data.Color(float(contents_list[4]), float(contents_list[5]), float(contents_list[6])),
                              data.Finish(float(contents_list[7]), float(contents_list[8]), float(contents_list[9]))))
                              

   eye_point = data.Point(0.0,0.0,-14.0) 
   light = data.Light(data.Point(-100.0,100.0,-100.0), data.Color(1.5,1.5,1.5))
   ambient = data.Color(1.0,1.0,1.0)
   min_x = -10
   max_x = 10
   min_y = -7.5
   max_y = 7.5
   width = 1024
   height = 762
                                 

   for i in range(3, len(argv)):

      #FOR -EYE
      if argv[i] is '-eye': 
         try: 
            x = float(argv[i+1])
         except: 
            x = 0.0
            
         try: 
            y = float(argv[i+2])
         except: 
            y = 0.0
            
         try: 
            z = float(argv[i+3])
         except: 
            z = -14.0
            
         eye_point = data.Point(x,y,z)
         
      #FOR -VIEW  
      if argv[i] is '-view': 
         
         try: 
            min_x = float(argv[i+1])
         except: 
            min_x = -10

         try: 
            max_x = float(argv[i+2])
         except: 
            max_x = 10

         try: 
            min_y = float(argv[i+3])
         except: 
            min_y = -7.5

         try: 
            max_y = float(argv[i+4])
         except: 
            max_y = 7.5

         try: 
            width = float(argv[i+5])
         except: 
            width = 1024

         try: 
            height = float(argv[i+6])
         except: 
            height = 762
            
      #FOR -LIGHT
      if argv[i] is '-light': 
         try: 
            x = float(argv[i+1])
         except: 
            x = -100.0
            
         try: 
            y = float(argv[i+2])
         except: 
            y = 100.0
            
         try: 
            z = float(argv[i+3])
         except: 
            z = -100.0
            
         try: 
            r = float(argv[i+4])
         except: 
            r = 1.5
               
         try: 
            g = float(argv[i+5])
         except: 
            g = 1.5
            
         try: 
            b = float(argv[i+6])
         except: 
            b = 1.5
            
         light = data.Light(data.Point(x,y,z), data.Color(r,g,b))
              
      #FOR -AMBIENT
      if argv[i] is '-ambient': 
         try: 
            r = float(argv[i+1])
         except: 
            r = 1.0
            
         try: 
            g = float(argv[i+2])
         except: 
            g = 1.0
            
         try: 
            b = float(argv[i+3])
         except: 
            b = 1.0
         
         ambient = data.Color(r,g,b)
    

   pixel_list = cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light)
   newf.write('P3\n')
   newf.write(str(width))
   newf.write(' ')
   newf.write(str(height))
   newf.write('\n255')
   for p in pixel_list: 
      newf.write('\n')
      newf.write(str(p[0]))
      newf.write(' ')
      newf.write(str(p[1]))
      newf.write(' ')
      newf.write(str(p[2]))
   newf.close()
   
exit()


  