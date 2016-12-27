import math

def open_file(name,mode):
   try:
      return open(name,mode)
   except:
      print 'Error--file could not be opened'
      exit()

def groups_of_3(list):
   newlist = []
   for i in range(0,len(list),3):
      if i+2 >= len(list):
         if i+1 >= len(list):
            newlist.append([list[i]])
         else:
            newlist.append([list[i],list[i+1]])
      else:
         newlist.append([list[i],list[i+1],list[i+2]])

   return newlist

def distance(x1,x2,y1,y2):
   return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def check_below_20(val):
   if val < 0.2:
      return 0.2
   else:
      return val

def process_file(f,row,col,radius):
   file_object = open('faded.ppm','w')

   long_list = []
   for line in f:
      a = line.split()
      for v in a:
         long_list.append(v)
   width = long_list[1]
   height = long_list[2]
   print>>file_object,long_list[0]
   print>>file_object,width,height
   print>>file_object,long_list[3]

   just_values = []
   for i in range(4,len(long_list)):
      just_values.append(long_list[i])

   grouped_pixels = groups_of_3(just_values)

   dist_list = []
   for y in range(int(height)):
      for x in range(int(width)):
         dist = distance(x,int(col),y,int(row))
         dist_list.append(dist)
   for i in range(len(grouped_pixels)):
      r = int(int(grouped_pixels[i][0]) * check_below_20(((int(radius)-dist_list[i])/int(radius))))
      g = int(int(grouped_pixels[i][1]) * check_below_20(((int(radius)-dist_list[i])/int(radius))))
      b = int(int(grouped_pixels[i][2]) * check_below_20(((int(radius)-dist_list[i])/int(radius))))

      print>>file_object, r,g,b 
