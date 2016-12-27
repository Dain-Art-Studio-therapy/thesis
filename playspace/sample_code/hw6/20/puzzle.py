import sys

def open_file(name,mode):
   try:
      return open(name,mode)
   except:
      print >> sys.stderr, '{0}:{1}'.format(name,"File does not exist")
      sys.exit(1)

def groups_of_3(list):
   newlist = []
   for i in range(0,len(list),3):
      if i+2 < len(list):
         newlist.append([list[i],list[i+1],list[i+2]])
   return newlist

def arg_check(argv):
   if len(argv) < 2:
      print >> sys.stderr, "File not provided"
      sys.exit(1)

def convert_color(list):
   r = list[0] * 10
   if r > 255:
      r = 255
   return r

def first_list(file):
   firstlist = []
   line = file.readlines()[3:]
   for l in line:
      pixels = l.split()
      for p in pixels:
         firstlist.append(int(p))
   return firstlist  

def main(argv):
   arg_check(argv)
   with open_file(argv[1], 'rb') as e:
      with open_file('hidden.ppm', 'w') as f:
         f.write("P3 ")
         f.write("500" + " " + "375")
         f.write(" 255 ")
         step1 = first_list(e)
         step2 = groups_of_3(step1)
         for x in step2:
            print >> f, convert_color(x), convert_color(x), convert_color(x)
   

if __name__ == '__main__':
   main(sys.argv)
