import sys
import math
def open_file(name,mode):
   try:
      return open(name,mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name,e.strerr)
      sys.exit(1)

def groups_of_3(list):
   newlist = []
   for i in range(0,len(list),3):
      if i+2 < len(list):
         newlist.append([list[i],list[i+1],list[i+2]])
   return newlist

def arg_check(argv):
   if len(argv) != 2 and len(argv) != 5:
      print >> sys.stderr, "Insuffcient number of arguments"
      sys.exit(1)

def list_combine(list,x,y):
   sum = 0
   newlist = []
   for row in range(int(y)):
      for col in range(int(x)):
         point = [row,col]
         list[sum].append(point)
         newlist.append(list[sum])
         sum = sum + 1
   return newlist

def distance(argv,list):
   d = math.sqrt((int(argv[2]) - list[3][0])**2 + (int(argv[3]) - list[3][1])**2)
   return d

def scale_color(argv,color,distance):
   s = ((int(argv[4]) - distance)/int(argv[4]))
   if s < 0.2:
      s = 0.2
   return color * s
   
def last_list(list,argv):
   final = []
   for l in list:
      d = distance(argv, l)
      a = scale_color(argv, l[0], d)
      b = scale_color(argv, l[1], d)
      c = scale_color(argv, l[2], d)
      final.append([a,b,c])
   return final

def get_w_h(argv):
   whlist = []
   with open_file(argv[1], 'rb') as g:
      info = g.readlines()[1:2]
      for i in info[0].split():
         whlist.append(int(i))
      return whlist

def main(argv):
   arg_check(argv)
   with open_file(argv[1], 'rb') as e:
      with open_file('faded.ppm', 'w') as f:
         l = get_w_h(argv)
         f.write("P3 ")
         f.write(str(l[0]) + " " + str(l[1]))
         f.write(" 255 ")
         line = e.readlines()[3:]
         firstlist = []
         for y in line:
            pixels = y.split()
            for p in pixels:
               firstlist.append(int(p))
         step1 = groups_of_3(firstlist)
         step2 = list_combine(step1,l[0],l[1])
         step3 = last_list(step2,argv)     
         for x in step3:
            print >> f, int(x[0]), int(x[1]), int(x[2]) 

if __name__ == '__main__':
   main(sys.argv)
