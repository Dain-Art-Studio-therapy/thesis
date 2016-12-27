import sys
import cast
import casting_test
import vector_math
import commandline
import data

def main(argv):
   count =0
   tally = 0
   real_flts = []
   sph_list = []
   vf_call = commandline.view_flag(argv)
   ef_call = commandline.eye_flag(argv)
   lf_call = commandline.light_flag(argv)
   af_call = commandline.ambient_flag(argv)
   try:
      f = open(argv[1], 'r')
      for line in f:
        indvl=line.split()
        count +=1
        if len(indvl) == 11:
          try:
            for element in indvl:
               real_flts.append(float(element))
            sph_list.append(data.Sphere
                            (data.Point(real_flts[0],real_flts[1],real_flts[2])
                             ,real_flts[3],data.Color(real_flts[4],real_flts[5]
                             ,real_flts[6]),data.Finish(real_flts[7],
                             real_flts[8],real_flts[9], real_flts[10])))
            real_flts = []
          except:
            print "malformed sphere on line" + str(count) + " .. skipping"
        else:
          print "malformed sphere on line" + str(count) + " .. skipping"
      cast.cast_all_rays(vf_call[0],vf_call[1],vf_call[2],vf_call[3],
                         vf_call[4],vf_call[5],data.Point(ef_call.x,ef_call.y,
                         ef_call.z),sph_list, data.Color(af_call.r,af_call.g,
                         af_call.b), data.Light(data.Point(lf_call.pt.x,
                         lf_call.pt.y,lf_call.pt.z), data.Color(lf_call.color.r,
                         lf_call.color.g,lf_call.color.b)))
      f.close()

                 
   except:
      print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"

if __name__ == "__main__":
   main(sys.argv)









