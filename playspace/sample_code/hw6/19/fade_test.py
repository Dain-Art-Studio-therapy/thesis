list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

width = 5
height = 2

for y in range(height):
   print '\n'
   for x in range(width):
      pixel = list[(y*width) + x]
      print pixel,
