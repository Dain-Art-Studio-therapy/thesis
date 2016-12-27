import sys
import math

def main():
   f = open_file()
   numlist = split_file_nums(f)
   #print numlist
   width = get_width(numlist)
   height = get_height(numlist)
   grouplist = groups_of_3(numlist)
   #print grouplist
   #print len(grouplist)
   twodlist = convert_2d(grouplist, width, height)
   #print twodlist
   #print len(twodlist)   
   reach = get_blur()
   fade_cast(twodlist, reach, numlist, width, height)

def fade_cast(twodlist, reach, numlist, width, height):
   finalfile = open('blurred.ppm', 'w')
   
   currentw = 0
   currenth = 0
   print >> finalfile, numlist[0]
   print >> finalfile, width, height
   print >> finalfile, numlist[3]
   
   counter = 0
   for i in range(height):
      for j in range(width):
         
         
         nearlist = get_nearby(j, i, twodlist, reach, width, height) 
         
         rsum = 0 
         gsum = 0
         bsum = 0
         counter = 0
         for k in nearlist:
             
             x = k[0]
             y = k[1]
             rsum += (twodlist[y][x][0])
             gsum += (twodlist[y][x][1])
             bsum += (twodlist[y][x][2])
             counter += 1
             
         print >> finalfile, int(rsum / counter)
         print >> finalfile, int(gsum / counter)
         print >> finalfile, int(bsum / counter)
         

def open_file():
   
   try:
      f = open(sys.argv[1], 'r')
      return f
   except:
      print 'Error: file does\'nt exist'
      exit()

def get_blur():
   
   arg = sys.argv
   try:
      return int(arg[2])

   except:
      return 4

def get_width(numlist):
   return int(numlist[1])

def get_height(numlist):
   return int(numlist[2])

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
         temp = [float(i) for i in trilist]
         grouplist.append(temp)
         del trilist[:]
      x += 1

   if len(trilist) > 0:
      grouplist.append(trilist)

   return grouplist

def convert_2d(grouplist, width, height):
   
   twodlist = []
   index = 0
   for y in range(height):
      twodlist.append([])
   for i in range(height):
      for j in range(width):
         twodlist[i].append(grouplist[index])
         index += 1
         
   return twodlist

def get_nearby(currentw, currenth, twodlist, reach, width, height):
   
   #initheight = check_init_parameter(currenth, reach)
   #initwidth = check_init_parameter(currentw, reach)
   #maxheight = check_final_parameter(currenth, reach, height)
   #maxwidth = check_final_parameter(currentw, reach, width)
   #print initheight
   #print initwidth
   #print maxheight
   #print maxwidth
   
   nearlist = []
   for i in range(max(currenth - reach, 0), min(currenth + reach, height)):
      for j in range(max(currentw - reach, 0), min(currentw + reach, width)):
        
         color = [j, i]
         nearlist.append(color)
        
    
   return nearlist 
   
def average_color(colorlist):
   colorsum = len(colorlist)
   rsum = 0
   gsum = 0
   bsum = 0
   for i in range(len(colorlist)):
      
      rsum += colorlist[i][0]
      gsum += colorlist[i][1]
      bsum += colorlist[i][2]
      
   averagecolor = [rsum / colorsum, gsum / colorsum, bsum / colorsum]
   return averagecolor
   


if __name__ == '__main__':
   main()
