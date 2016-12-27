import sys

def groups_of_3(input):
    newList = []
    for i in range(0, len(input), 3):
        if i+3>len(input):
            if ((i+3) - len(input) == 1):
                newList.append(input[i:i+2])
            elif ((i+3) - len(input) == 2):
                newList.append([input[i]])
        else:
            newList.append(input[i:i+3])
    return newList

def open_file(filename, mode):
   try:
     return open(filename, mode)
   except IOError as e:
      print>>sys.stderr, '{0}:{1}'.format(filename, e.strerror)

def cap_color_values(number):
   if number>255:
      return 255
   else:
      return number

def validate_args(argv, length):
   if len(argv) != length:
      print>>sys.stderr, 'not enough arguments'
      exit(1)

def process_file(in_file, out_file):
   line_counter = 0
   extra = []
   for line in in_file:
      if line_counter < 3:
         print>>out_file, line
      if line_counter >= 3:
         stringer = line.split()
         if extra == []:
            list_of_line_in_3 = groups_of_3(stringer)
            for l in list_of_line_in_3:
               if len(l) == 3:
                  try:
                     r = int(l[0]) * 10
                     new_r = cap_color_values(r)
                     extra = []
                     print>>out_file, new_r, new_r, new_r
                  except:
                     print>>sys.stderr, 'Line', line_counter, 'unable to convert'
               else:
                  extra = l                 
         else:
            for i in stringer:
               extra.append(i)
            list_of_line_in_3 = groups_of_3(extra)
            for l in list_of_line_in_3:
               if len(l) == 3:
                  try:
                     r = int(l[0]) * 10
                     new_r = cap_color_values(r)
                     extra = []
                     print>>out_file, new_r, new_r, new_r
                  except:
                     print>>sys.stderr, 'Line', line_counter, 'unable to convert'
               else: extra = l                   
      line_counter += 1            
   
def main(argv):
   validate_args(argv, 2)
   OUT_FILE = open_file('hidden.ppm', 'wb')
   with open_file(argv[1], 'rb') as f:
      process_file(f, OUT_FILE) 

if __name__ == '__main__':
   main(sys.argv)
