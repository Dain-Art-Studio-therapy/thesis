import sys

def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         file_list = make_list(f)
         colors = grouper(file_list)
         writer(file_list, colors)
   except:
      print 'file not provided'

def make_list(fil):
   newlist = []
   for line in fil:
      s = line.split()
      for n in s:
         newlist.append(n)
   return newlist

def grouper(l):
   newlist = []
   for i in range(4, len(l), 3):
      color = int(l[i]) * 10
      if color > 255:
         color = 255
      newlist.append((color, color, color))
   return newlist

def writer(text, threes):
   with open('hidden.ppm', 'w') as f:
      print >>f, 'P3'
      print >>f, text[1], text[2]
      print >>f, text[3]
      for n in threes:
         print >>f, n[0], n[1], n[2]

if __name__=='__main__':
   main(sys.argv)
