import sys

DEFAULT_BLUR = 4

def process(argv):
   validate_cmdline(argv) 
   picture = []
   with open_file(argv[1], 'rb') as f:
      picture = process_file(f)
   blur = command_flags(argv)
   return [picture, blur]
   
def validate_cmdline(argv):
   if len(argv) >= 2:
      pass
   else:
      print 'usage: python puzzle.py <file> [-blur factor (int)]'
      exit(1)

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      exit(1)

def process_file(f):
   file = f.read()
   n = file.split()
   header = n[0:4]
   pixels = process_pixels(n[4:])
   return [header, pixels]

def process_pixels(pixels):
   N = [pixels[i:i+3] for i in range(0, len(pixels), 3)]
   return N

def command_flags(argv):
   if len(argv) == 3:
      return try_blur(argv[2])
   else:
      return DEFAULT_BLUR

def try_blur(str):
   try:
      return int(str)
   except:
      print 'Invalid entry for blur - non-integer'
      return DEFAULT_BLUR

if __name__ == '__main__':
   process(sys.argv)
