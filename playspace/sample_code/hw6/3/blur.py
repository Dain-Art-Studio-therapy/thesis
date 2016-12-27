import sys

OUTFILE = 'blurred.ppm'

def main(argv):
	checkArgs(argv)
	
	infile = open(argv[1], "r")
	outfile = open(OUTFILE, "w")
	
	header = getHeader(infile)
	writeHeader(outfile, header)
	
	blurFactor = getBlurFactor(argv)
	pMap = getPixels(infile, header)
	
	pMap = blurPixels(pMap, blurFactor)
	printMap(pMap, outfile)
		
	outfile.close()
	infile.close()

def printMap(pMap, outfile):
	for i in range(len(pMap)):
		for j in range(len(pMap[0])):
			outfile.write(str(pMap[i][j][0]) + " " +\
						  str(pMap[i][j][1]) + " " +\
						  str(pMap[i][j][2]) + "\n")
	
def blurPixels(pMap, blurFactor):
	for i in range(len(pMap)):
		for j in range(len(pMap[0])):
			red = []
			green = []
			blue = []
			for k in range(i - blurFactor, i + blurFactor + 1):
				for l in range(j - blurFactor, j + blurFactor + 1):
					try:
						red.append(int(pMap[k][l][0]))
						green.append(int(pMap[k][l][1]))
						blue.append(int(pMap[k][l][2]))
					except:
						pass
			pMap[i][j] = (int(sum(red) / float(len(red))),\
						  int(sum(green) / float(len(green))),\
						  int(sum(blue) / float(len(blue))))
	return pMap
						  
def getBlurFactor(argv):
	if len(argv) == 2:
		return 4
	else:
		return argv[2]
	
def getPixels(infile, header):
	width = int(header[1])
	height = int(header[2])
	pMap = []
	for i in range(height):
		pMap.append([])
		for j in range(width):
			pMap[i].append(getNextPixel(infile))
	return pMap
	
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
	if len(argv) != 2 and len(argv) != 3:
		sys.exit("Invalid arguments")
	
	checkFile(argv[1])
	
	if len(argv) == 3:
		try:
			a2 = int(argv[2])
			if a2 != float(argv[2]):
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