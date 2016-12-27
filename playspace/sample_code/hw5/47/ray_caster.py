import sys
from cast import * 
from data import * 
from commandline import *
def main(argv):
   try: 
      with open(argv[1],"r") as file:
         A =  readIn_sphere(file)
      ray_caster(argv,A)
   except:
      print ("usage: python ray_caster.py <filename> [-eye x y z]"  
      "[-view min_x max_x min_y width height] [-light x y z r g b]"  
     " [-ambient r g b] ")
  # ray_caster(argv,A)   


def readIn_sphere(file):
   counter= 0 
   list_sph = [ ]
    
    
   for line in file:
      counter = counter + 1
      
      try:
         list = line.split()
         x = float(list[0])
         y = float(list[1])
         z = float(list[2])
     
         radius = float(list[3])
         r = float(list[4])
         g = float(list[5])
         b = float(list[6])
         
 
         ambient = float(list[7])
         diffuse = float(list[8])
         specular = float(list[9])
         roughness = float(list[10])
   
         center = Point(x,y,z)
         sph_color = Color(r,g,b)
         sph_finish = Finish(ambient,diffuse,specular,roughness)
         

         list_sph.append(Sphere(center,radius,sph_color,sph_finish))
        
           


      except:
          print  "Malformed Sphere on line:"+str(counter) + ".....skipping"
   
   return list_sph
    
def ray_caster(argv,sphere_list):
    def_eye = Point(0.0,0.0,-14.0)
    def_light= Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
    def_ambient= Color(1.0,1.0,1.0)
    def_view = [-10,10,-7.5,7.5,1024,768]
              #[min_x,max_x,min_y,max_y,width,height]
    

        
        
    for index in range(len(argv)):
        if argv[index] == "-eye":
           
            new_eye=eye(argv,index)
            def_eye = new_eye
           
            
                         
                
        elif argv[index] == "-light":
            
           new_light =light(argv,index) 
           def_light = new_light
          
        
        
            
        elif argv[index] == "-ambient":
           new_ambient =ambient(argv,index)
           def_ambient = new_ambient
        
            
        elif argv[index] == "-view":
            new_view = view(argv,index)
            def_view[0] = new_view[0]
            def_view[1] = new_view[1]
            def_view[2] = new_view[2]
            def_view[3] = new_view[3]
            def_view[4] = new_view[4]
            def_view[5] = new_view[5]
            
     
     
    cast_all_rays(def_view[0],def_view[1],def_view[2],def_view[3],def_view[4]\
                  ,def_view[5],def_eye,sphere_list,def_ambient,def_light)
            

    
if __name__ == '__main__':
   main(sys.argv)
