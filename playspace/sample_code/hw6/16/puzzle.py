import sys


def main():
   f = open_file()
   numlist = split_file_nums(f)
   
   grouplist = groups_of_3(numlist)
   
   puzzle_cast(numlist, grouplist)


def puzzle_cast(numlist, grouplist):
   finalfile = open('hidden.ppm', 'w')
   
   width = int(numlist[1])
   height = int(numlist[2])
   print >> finalfile, numlist[0]
   print >> finalfile, width, height
   print >> finalfile, numlist[3]
   

   for i in grouplist:
      alteredcolor = alter_color(i)
      print >> finalfile, int(alteredcolor[0])
      print >> finalfile, int(alteredcolor[1])
      print >> finalfile, int(alteredcolor[2])


def open_file():
   try:
      f = open(sys.argv[1], 'r')
      return f
   except:
      print 'Error: file does\'nt exist'
      exit()
   
   

def split_file_nums(f):
   
   numlist = []
  
   for line in f:
      nums = line.split()
      for i in nums:
         numlist.append(i)
      
   return numlist

def groups_of_3(numlist):

   if numlist == []:
      return None
   grouplist = []
   
   newnum = numlist[4:]
   x = 0
   
   trilist = []
   while x < len(newnum):
      trilist.append(newnum[x])
      if len(trilist) == 3:
         temp = [i for i in trilist]
         grouplist.append(temp)
         del trilist[:]
      x += 1

   if len(trilist) > 0:
      grouplist.append(trilist)

   return grouplist

def alter_color(color):

   rAlter = min(int(color[0]) * 10, 255)
   
   alteredcolor = [rAlter, rAlter, rAlter]
      

   return alteredcolor

if __name__ == '__main__':
   main()



