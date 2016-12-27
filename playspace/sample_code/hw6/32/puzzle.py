from sys import argv
import sys

def main(argv):
   try:
        with open('hidden.ppm', 'w') as output:
              return read(argv, output)
   except IndexError:
       print >> sys.stderr, 'parameter not received'
       exit()
   except AttributeError:
       print >> sys.stderr, 'completed'
       exit()
   except TypeError:
       print >> sys.stderr, 'completed'
       exit()

def read(argv, output):
   try:
       with open(argv[1], 'r') as input:
            return readFile(argv, output)
   except IOError:
       print >> sys.stderr, 'file could not be opened'
       exit()

def readFile(input, output):
    values = input.read().split()
    for index in range(len(values)):
        if index < 4:
            print >> output, str(values[index])
        elif (index-1) % 3 == 0:
            value = int(values[index]) * 10
            if value > 255:
                value = 255
            print >> output, str(value)
        else:
            print >> output, str(value)

if __name__ == '__main__':
    main(argv)


