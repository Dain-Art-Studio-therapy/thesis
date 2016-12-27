import sys

def parseargs(argv):
   if len(argv) <= 1:
      print "Give an file name"
      exit(1)
   else:
      with open_file(argv[1], 'rb') as f:
         linearray = []
         for line in f:
            linearray.append(line.replace('\n', ''))
         threes = groups_of_3(linearray)
         header = threes[0]
         del threes[0]
         values = get_decoded_values(threes)
         write_ppm(header, values)

def get_decoded_values(threes):
   final_colors = []
   for three in threes:
      try:
         final = float(three[0])*10
         if final > 255:
            final = 255
         for x in range(0, 3):
            final_colors.append(str(final))
            final_colors.append(' ')
      except:
         print "Non number found"
   return final_colors


def write_ppm(header, values):
   with open('hidden.ppm', 'w') as f:
      f.write(header[0] + '\n' + header[1] + '\n' + header[2] + '\n')
      f.write(''.join(values))

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def groups_of_3(values):
   if values == []:
      return -1
   else:
      return [values[i:i+3] for i in range(0, len(values), 3)]

if __name__ == "__main__":
   parseargs(sys.argv)
