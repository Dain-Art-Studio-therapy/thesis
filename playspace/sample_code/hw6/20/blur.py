import sys
import math
def open_file(name,mode):
   try:
      return open(name,mode)
   except:
      print >> sys.stderr, '{0}:{1}'.format(name, 'File does not exist')
      sys.exit(1)

def groups_of_3(list):
   newlist = []
   for i in range(0,len(list),3):
      if i+2 < len(list):
         newlist.append([list[i],list[i+1],list[i+2]])
   return newlist

def arg_check(argv):
   if len(argv) != 3:
      argv[2] = 4

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

def blur_list(list,argv):
   for i in range(len(list)):
      x = list[i][3][0] + (2 * int(argv[2]))
      y = list[i][3][1] + (2 * int(argv[2]))
      list[i][3][0] = x
      list[i][3][1] = y
   return list

def average_list(list,argv):
   for i in range(len(list)):
      area = (1 + (2 * int(argv[2])))**2
      list[i][0] = (list[i][0]/area)
      list[i][1] = (list[i][1]/area)
      list[i][2] = (list[i][2]/area)
   return list

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
      with open_file('blurred.ppm', 'w') as f:
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
         step3 = blur_list(step2,argv)
         step4 = average_list(step3,argv)
         for x in step4:
            for i in range(len(x)):
               print >> f, x[i]

if __name__ == '__main__':
   main(sys.argv)



