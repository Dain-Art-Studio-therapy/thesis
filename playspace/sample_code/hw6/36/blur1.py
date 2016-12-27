#blur
#slow version
#seems to give the correct image, but takes so long i didnt wait to be sure
import sys

BLUR_DEFAULT = 4

def main(argv):
  if len(argv) < 2 or len(argv) > 3:
    print 'Error: usage: python blur.py <filename> [blur_amount]'
  else:
    blur_amt = cmdline_blur(argv)
    with open_file(argv[1], 'rb') as input:
      process_file(input, BLUR_DEFAULT)

def cmdline_blur(argv):
  try: return int(argv[2])
  except: return 4

def process_file(file, blur_amt):
  f = file.read()
  print_header(f)
  WIDTH = int(f.split( )[1])-1
  blur(group3(f), WIDTH, blur_amt)

def blur(pixel_list, WIDTH, blur):
  p_p_list = pixel_position_list(pixel_list, WIDTH)
  for i in p_p_list:
    average_pixel_color(pixel_list_to_average(i[0], p_p_list, blur))

  
def average_pixel_color(pix_list):
  tot_r = 0
  tot_g = 0
  tot_b = 0
  tot_pix = 0
  blurred = open_file('blurred.ppm', 'a')  
  for p in pix_list:
    tot_r += p[0]
    tot_g += p[1]
    tot_b += p[2]
    tot_pix += 1
  print >> blurred, tot_r/tot_pix, tot_g/tot_pix, tot_b/tot_pix

def pixel_list_to_average(pixel_pos, pix_pos_list, blur):
  p_list_to_avg = []
  for i in pix_pos_list:
    if within_b(i[0][0], i[0][1], pixel_pos[0], pixel_pos[1], blur) == True:
      p_list_to_avg.append(i[1])
  return p_list_to_avg

def within_b(x1, y1, x2, y2, blur):
  if (x1 <= x2+blur and x1 >= x2 - blur and
      y1 <= y2 + blur and y1 >= y2 - blur):
    return True
  else: return False


def pixel_position_list(pixel_list, WIDTH):
  row = 0
  col = 0
  pix_pos_list = []
  for i in pixel_list:
    pix_pos_list.append(([col, row], i))
    if col == WIDTH:
      col = 0
      row +=1
    else: col +=1
  return pix_pos_list




def print_header(string):
  blurred = open_file('blurred.ppm', 'w')
  l = string.split( )
  print >> blurred, l[0]
  print >> blurred, l[1], l[2]
  print >> blurred, l[3]

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
  for e in range(4, len(l)-1):
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


