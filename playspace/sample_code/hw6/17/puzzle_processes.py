def process_file(f, width):
   unsorted = f.read().split()
   pixels = groups_of_n(groups_of_n(unsorted,3),width)
   return decode_pixels(pixels)

# list of list of list of numbers. -> list of list of list of numbers
# in other words, grouped, ordered pixels -> grouped ordered pixels
def decode_pixels(pixels):
   decoded = []
   curRow = 0
   for row in pixels:
      decoded.append([])
      for col in row:
         decoded[curRow].append([min(255, int(col[0]) * 10), min(255, int(col[0]) * 10),
            min(255, int(col[0]) * 10)])
      curRow += 1
   return decoded


def print_header(size, maxColor, output):
   print >> output, 'P3'
   print >> output, size[0], size[1]
   print >> output, maxColor

def print_pixels(pixels, output):
   for row in pixels:
      for col in row:
         for color in col:
            print >> output, color,
      print >> output, ''

# takes in a list of values and returns a grouped list of values
def groups_of_n(list, n):
   grouped = []
   curGroup = -1
   
   for i in range(len(list)):
      if i % n == 0:
         grouped.append([list[i]])
         curGroup += 1
      else: 
         grouped[curGroup].append(list[i])
   return grouped
