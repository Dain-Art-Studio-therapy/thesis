import sys
import groups

width = 1024
height = 768

def main(argv):
   try:
      in_file = argv[1]
      open(in_file)
   except:
      print 'no input image'
      sys.exit()
   with open('hidden.ppm', 'w+')as out_pic:
      with open(in_file, 'r')as in_pic:

         out_pic.write('P3''\n')
         out_pic.write(str(500)+" "+str(375)+'\n')
         out_pic.write('255''\n')

         just_numbers = []
         for line_num in range(3):
            in_pic.next()
         for line in in_pic:
               just_numbers.append(int(line))
         #print just_numbers
         in_three_tuples = groups.groups_of_three(just_numbers)
         #print in_three_tuples[0]
      return_list = []
      for item in in_three_tuples:
         num = str(item[0] * 10)
         if item[0] > 25.5:
            out_pic.write('255'+" "+'255'+" "+'255'+'\n')
         else:
            out_pic.write(num+" "+num+" "+num+'\n')


      #print list(in_pic.read())
   #print in_three_tuples[0]
   #print 
   #print just_numbers

if __name__ == '__main__':
   main(sys.argv)