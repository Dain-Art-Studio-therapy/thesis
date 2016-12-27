import sys

def groups_of_3(l):
   final_list_length = len(l) % 3
   new_list = []
   x = 0
   while x < (len(l) - final_list_length):
      new_list.append([l[x], l[x+1], l[x+2]])
      x += 3
   if (final_list_length == 2):
      new_list.append([l[len(l)-final_list_length], l[len(l)-1]])
   if (final_list_length == 1):
      new_list.append([l[len(l)-1]])
   return new_list

def setup_file(filename, width_image, height_image):
    output = open(filename, 'w')
    output.write("P3\n")
    output.write(str(width_image)+" " + str(height_image) + "\n")
    output.write("255\n")
    return output
   
def test_args(argv):
    try:
        file_to_open = argv[1]
    except:
        sys.stderr.write('Proper syntax is: python puzzle.py <filename>\n')
        sys.stderr.write('Invalid file name specified. Exiting.\n')
        exit()
    return file_to_open

def adjust_color_component(i):
    i[0] = i[0] * 10
    if (i[0] > 255):
        i[0] = 255
    i[1] = i[0]
    i[2] = i[0]
    return i

def print_pts(i,output):
    output.write(str(int(i[0]))+" "+str(int(i[1]))+" "+str(int(i[2]))+"\n")
   
def main(argv):
    file_to_open = test_args(argv)
    try:
       with open(file_to_open, 'r') as f:
           l = []
           i = 0
           for line in f:
               i+=1
               if i == 2:
                  lin = line.split()
                  width_image = int(lin[0])
                  height_image = int(lin[1])
               if i >= 4:
                   l.append(float(line))
    except:
        sys.stderr.write('Error parsing file. Verify validity of \
file syntax.\n')
        exit()
    l = groups_of_3(l)
        
    output = setup_file('hidden.ppm', width_image, height_image)
    for i in l:
        i = adjust_color_component(i)
        print_pts(i,output)

main(sys.argv)
