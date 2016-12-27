#puzzle

import sys

def main(argv):
  if len(argv) < 2:
    print 'Error: usage: python puzzle.py <filename>'
  else:
    with open_file(argv[1], 'rb') as input:
      process_file(input)

def process_file(file):
  f = file.read()
  print_header(f)
  decode(group3(f))

def print_header(string):
  hidden = open_file('hidden.ppm', 'w')
  l = string.split( )
  print >> hidden, l[0]
  print >> hidden, l[1], l[2]
  print >> hidden, l[3]  


def decode(lists):
  hidden = open_file('hidden.ppm', 'a')
  for i in lists:
    g = (i[0]*10)
    if g > 255: g = 255
    print >> hidden, g, g, g

def open_file(file_name, mode):
  try:
    return open(file_name, mode)
  except IOError as e:
    print >> sys.stderr, 'Error: Cannot Open File'. format(file_name,
       e.strerror)
    exit(1)

def is_int(x):
  try: 
    return int(x)
  except:
    print 'Error: improperly formatted image file'
    return 0

def group3(string):
  l = string.split( )
  g = []
  for e in range(4, len(l)):
    g.append(is_int(l[e]))
  return groups_of_3(g)

def groups_of_3(list):
  g = []
  if len(list)==0:
    return [g]
  elif len(list)==1:
    return [list]
  elif len(list)==2:
    return[[list[0], list[1]]]

  for v in range(3, len(list), 3):
      g.append([list[v-3], list[v-2], list[v-1]])

  if len(list)%3==0:
    g.append([list[len(list)-3], list[len(list)-2], list[len(list)-1]])
    return g
  elif len(list)%3==1:
    g.append([list[len(list)-1]])
    return g
  elif len(list)%3==2:
    g.append([list[len(list)-2], list[len(list)-1]])
    return g


if __name__ == '__main__':
   main(sys.argv)


