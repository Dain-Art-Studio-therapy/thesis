from sys import *


def read_header(list, output_file):
   print >> output_file, list[0]
   print >> output_file, list[1],list[2]
   print >> output_file, list[3]


def read_through(file_name):
   f = file_name.read()
   list = f.split()
   return list

def groups_of_3(list_of_values):
   groups = []
   current_group = []
   cur_group_length = 3
   for i in range(4,len(list_of_values),cur_group_length):
      groups = list_of_values[i:i+cur_group_length]
      current_group.append(groups)
   return current_group
  

def open_file(file_name):
   try:
      f = open(file_name, "r")
   except:
      print 'Error couldnt open hidden.ppm'
      exit()




def open_file2(file_name):
   try:
      f = open(file_name, "w")
   except:
      print 'Error couldnt open hidden.ppm'
      exit()
      

def mult_red(new_list,out_file):
   for i in range(len(new_list)):
      r = min(int(new_list[i][0]) * 3,255)
      R = str(r)
      print >> out_file,R,R,R
#(str(min(new_pixel[0],255)) + ' '  +  str(min(new_pixel[1],255)) + ' ' +  str(min(new_pixel[2],255)) + '\n')

def main():
   try:
      f = open(argv[1],'r')
   except:
      print 'error'
   A = open('hidden.ppm','w')
   a = read_through(f)
   read_header(a,A)
   c = groups_of_3(a)
   mult_red(c,A)
   

if __name__ == '__main__':
   main()


