import sys
import math

OUTFILE = 'faded.ppm'

def main(argv):
	checkArgs(argv)
	
	infile = open(argv[1], "r")
	outfile = open(OUTFILE, "w")
	
	header = getHeader(infile)
	writeHeader(outfile, header)
	
	location = [0, 0] # row, column
	fade = getFade(argv)
	
	pixel = getNextPixel(infile)
	while pixel != (None, None, None):
		pixel = fadePixel(pixel, fade, location)
		writePixel(outfile, pixel)
		pixel = getNextPixel(infile)
		location = updateLocation(location, header)
		
	outfile.close()
	infile.close()

def distance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
	
def updateLocation(location, header):
	location[1] += 1
	if location[1] >= int(header[1]):
		location[1] = 0
		location[0] += 1
	return location

def fadePixel(pixel, fade, location):
	scale = 1 - distance(location, (fade[0], fade[1])) / fade[2]
	if scale < 0.2:
		scale = 0.2
	return (str(int(float(pixel[0]) * scale)),\
		    str(int(float(pixel[1]) * scale)),\
		    str(int(float(pixel[2]) * scale)))
	
def getFade(argv):
	return (int(argv[2]), int(argv[3]), int(argv[4]))
	
def writePixel(outfile, pixel):
	outfile.write(pixel[0] + " " + pixel[1] + " " +\
				  pixel[2] + "\n")
	
def writeHeader(outfile, header):
	outfile.write(header[0] + "\n" + header[1] + " " +\
				  header[2] + "\n" + header[3] + "\n")
	
def getNextPixel(infile):
	pixel = (getNextParam(infile),\
			 getNextParam(infile),\
			 getNextParam(infile))
	return pixel
	
def getHeader(infile):
	header = (getNextParam(infile),\
			  getNextParam(infile),\
			  getNextParam(infile),\
			  getNextParam(infile))
	return header
	
def getNextParam(infile):
	string = ''
	c = infile.read(1)
	if c == '':
		return None
	while len(string) <= 3 and c != ' ' and c != '\n':
		string += c
		c = infile.read(1)
	return string
	
def checkArgs(argv):
	if len(argv) != 5:
		sys.exit("Invalid arguments")
	checkFile(argv[1])
	
	try:
		a2 = int(argv[2])
		a3 = int(argv[3])
		a4 = int(argv[4])
		if a2 != float(argv[2]) or\
		   a3 != float(argv[3]) or\
		   a4 != float(argv[4]):
			sys.exit()
	except:
		sys.exit("Invalid arguments")

def checkFile(fileName):	
	try:
		f = open(fileName)
		f.close()
	except:
		sys.exit("Error : File cannot be opened.")
	
if __name__ == "__main__":
	main(sys.argv)