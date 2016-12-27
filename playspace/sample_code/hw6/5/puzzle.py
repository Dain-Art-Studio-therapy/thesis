import sys

def open_infile(argv):
   try:
      infile = open(argv[1], "rb")
      return infile
   except IOError as e:
      print "File is missing or does not exist"
      exit(1)

def open_outfile(output_file):
   try:
      outfile = open(output_file, "w")
      return outfile
   except IOError as e:
      print "File cannot be opened for writing"
      exit(1)

def group_pixels(input_file):
   pixel_group = []
   for i in range(0,len(input_file),3):
      increment = i + 3
      pixel_group.append(input_file[i:increment])
   return pixel_group

def read_image(infile):
   full_read = infile.read()
   full_split = full_read.split()
   return full_split

def translate_pixel(pixel):
   translated_r = int(pixel[0]) * 10
   if translated_r >= 255:
      translated_r = 255
   return translated_r

def output_pixels(split_file, outfile):
   p3_header = split_file[0]
   width = split_file[1]
   height = split_file[2]
   max_color = split_file[3]
   print >> outfile, p3_header
   print >> outfile, width, height
   print >> outfile, max_color
   pixel_groups = group_pixels(split_file[4:])
   for pixel in pixel_groups:
      new_p = translate_pixel(pixel)
      print >> outfile, new_p, new_p, new_p

def main(argv):
   infile = open_infile(argv)
   full_image = read_image(infile)
   outfile = open_outfile("hidden.ppm")
   output_pixels(full_image, outfile)
   outfile.close()

if __name__ == '__main__':
   main(sys.argv)
