import sys
import data
import commandline
import cast
import data
from commandline import test_argvs_float

def main(argv):
   if len(argv) == 1:
      print 'usage: python ray_caster.py <filename> -eye x y z -view min_x max_x min_y max_y width height -light x y z r g b -ambient r g b'
   elif len(argv) == 2:
      eye_point = data.Point(0.0,0.0,-14)
      min_x = -10
      max_x= 10
      min_y = -7.5
      max_y = 7.5
      width = 1024
      height = 768
      light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))
      ambient = data.Color(1.0,1.0,1.0)
   elif len(argv) > 2:
      eye_point = data.Point(0.0,0.0,-14.0)
      min_x = -10
      max_x = 10
      min_y = -7.5
      max_y = 7.5
      width = 1024
      height = 768
      light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))
      ambient = data.Color(1.0,1.0,1.0)

      for i in range(2,len(argv)):
         if argv[i] == '-eye':
            try:
               x = test_argvs_float(argv[i+1],0.0)
               y = test_argvs_float(argv[i+2],0.0)
               z = test_argvs_float(argv[i+3],-14.0)
               eye_point = data.Point(x,y,z)   
            except:
               eye_point = data.Point(0.0,0.0,-14.0)

         if argv[i] == '-view':
            try:
               min_x = test_argvs_float(argv[i+1],-10)
               max_x = test_argvs_float(argv[i+2],10)
               min_y = test_argvs_float(argv[i+3],-7.5)
               max_y = test_argvs_float(argv[i+4],7.5)
               width = test_argvs_int(argv[i+5],1024)
               height = test_argvs_int(argv[i+6],768)
            except:
               min_x = -10
               max_x = 10
               min_y = -7.5
               max_y = 7.5
               width = 1024
               height = 768
                  
         if argv[i] == '-light':
            try:
               lx = test_argvs_float(argv[i+1],-100.0)
               ly = test_argvs_float(argv[i+2],100.0)
               lz = test_argvs_float(argv[i+3],-100.0)
               lr = test_argvs_float(argv[i+4],1.5)
               lg = test_argvs_float(argv[i+5],1.5)
               lb = test_argvs_float(argv[i+6],1.5)
               light = data.Light(data.Point(lx,ly,lz),data.Color(lr,lg,lb))
            except:
               light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))   
                  
         if argv[i] == '-ambient':
            try: 
               ar = test_argvs_float(argv[i+1],1.0)
               ag = test_argvs_float(argv[i+2],1.0)
               ab = test_argvs_float(argvs[i+3],1.0)
               ambient = data.Color(ar,ag,ab)
            except:
               ambient = data.Color(1.0,1.0,1.0)        
         
   with commandline.open_file(argv[1],'rb') as f:
      sphere_list = commandline.process_file(f)
      generated_image=cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient,light)
      return generated_image






if __name__ == '__main__':
   main(sys.argv)
