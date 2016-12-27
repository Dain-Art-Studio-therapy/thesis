#fade

import sys

WIDTH = 0

def main(argv):
  if len(argv) < 5:
    print 'Error: usage: python fade.py <filename> row column radius'
  else:
    try:
      int(argv[2]) and int(argv[3]) and int(argv[4])
    except: 
      print 'Error: row, column, and radius must be integers'
      exit(1)
    with open_file(argv[1], 'rb') as input:
      fade_info = [argv[3], argv[2], argv[4]]
      process_file(input, fade_info)


def process_file(file, fade_info):
  f = file.read()
  print_header(f)
  WIDTH = int(f.split( )[1])-1
  pixel_fade(group3(f), fade_info, WIDTH)

def fader_at_point(pixel_position, fade_info):
  fx = is_int(fade_info[0])
  fy = is_int(fade_info[1])
  rad = is_int(fade_info[2])
  px = is_int(pixel_position[0])
  py = is_int(pixel_position[1])
  dist = distance([px,py], [fx, fy])
  mult = (rad - dist)/rad
  if mult < 0.2: mult = 0.2
  return mult

def fade_col(col, mult):
  x = int(col*mult)
  if x > 255: x = 255
  return x

def pixel_fade(pixel_list, fade_info, WIDTH):
  row = 0
  col = 0
  g = []
  faded = open_file('faded.ppm', 'a')
  for i in pixel_list:
    m = fader_at_point([col, row], [fade_info[0], fade_info[1], fade_info[2]])
    for c in i:
      is_int(c)
      print >> faded, fade_col(c,m)
    if col == WIDTH:
      col = 0
      row +=1
    else: col +=1

def distance(p1, p2):
  dist = (((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**0.5
  return dist

def print_header(string):
  faded = open_file('faded.ppm', 'w')
  l = string.split( )
  print >> faded, l[0]
  print >> faded, l[1], l[2]
  print >> faded, l[3]
  global WIDTH
  WIDTH = l[1]
  return WIDTH


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


