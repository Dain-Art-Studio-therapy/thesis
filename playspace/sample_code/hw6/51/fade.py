from groups import *
import sys
import math

def openfile(argv):
   try:
      f=open(argv[1])
      return f
   except:
      print 'Please enter a valid file name.'
      exit(1)

def calc_dist(pt_x,pt_y,pxl_x,pxl_y):
   return math.sqrt(float((pxl_x-pt_x)**2+(pxl_y-pt_y)**2))

def scale_color(scale,color):
   if scale<.2:
      scale=.2
   r=int(color[0])*scale
   g=int(color[1])*scale
   b=int(color[2])*scale
   return (int(r),int(g),int(b))

def fade_image(colors,argv,wid,hei):
   final=[]
   pt_x=int(argv[3])
   pt_y=int(argv[2])
   rad=int(argv[4])
   color_groups=groups_of_3(colors)
   for i in range(len(color_groups)):
      pxl_x=i%wid
      pxl_y=(i-pxl_x)/(wid)
      dist=calc_dist(pt_x,pt_y,pxl_x,pxl_y)
      scale=(rad-dist)/rad
      new_color=scale_color(scale,color_groups[i])
      final.append(str(int(new_color[0])))
      final.append(' ')
      final.append(str(int(new_color[1])))
      final.append(' ')
      final.append(str(int(new_color[2])))
      final.append('\n')
   return ''.join(final)

def read_values(file):
   contents_list=[]
   for line in file:
      contents_list.append(line.split())
   contents=[]
   for i in contents_list:
      for j in range(len(i)):
         contents.append(i[j])
   return contents

def read_colors(values):
   return values[4:len(values)]

def main(argv):
   o=openfile(argv)
   values=read_values(o)
   wid=int(values[1])
   hei=int(values[2])
   colors=read_colors(values)
   with open('faded.ppm','w') as fin:
      print >> fin, 'P3\n'+str(wid)+' '+str(hei)+'\n'+'255\n'
      print >> fin, fade_image(colors,argv,wid,hei)
   o.close()

if __name__ == '__main__':
   main(sys.argv)