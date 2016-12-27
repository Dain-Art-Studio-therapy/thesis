from sys import *
import data
import cast
import commandline


def main(argv):
   slist = []
   try:
      fh = open(argv[1] , "r")
   except:
      print "Error Opening File"
      exit()

   
   count = 1
   for line in fh:
      try:
         values = line.split()        
         if len(values) == 11:
            vals = [float(n) for n in values]
            sce_x        = vals[0]
            sce_y        = vals[1]
            sce_z        = vals[2]
            srad         = vals[3]
            sc_r         = vals[4]
            sc_g         = vals[5]
            sc_b         = vals[6]
            sfi_ambient  = vals[7]
            sfi_diffuse  = vals[8]
            sfi_specular = vals[9]
            sfi_rou= vals[10]

            sfinish= data.Finish(sfi_ambient,sfi_diffuse, sfi_specular, sfi_rou)

            spoint = data.Point(sce_x,sce_y,sce_z) 

            scolor = data.Color(sc_r,sc_g,sc_b)

            sphere = data.Sphere(spoint,srad, scolor, sfinish)

            slist.append(sphere)
         else:
            raise
         count = count + 1
      except:
         print "Malphormed Sphere...Skipping Line " + str(count)
         count = count + 1
         
   return slist

call = main(argv)
f = commandline.flags() 
cast.cast_all_rays(f[0],f[1],f[2],f[3],f[4],f[5],f[6],call,f[7],f[8])


if __name__ == "__main__":
   main(argv)
