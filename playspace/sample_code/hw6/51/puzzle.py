import sys
from groups import *

def openfile(argv):
	try:
		f=open(argv[1])
		return f
	except:
		print 'Please enter a valid file name.'
		exit(1)

def orig_colors(orig):
	final=[]
	for i in range(3,len(orig)):
		final.append(orig[i])
	return final

def decode(orig):
	final=[]
	rows=groups_of_3(orig)
	#count=0
	for c in rows:
		#if count%3==0:
		red=int(c[0][0])*10
		if red>255:
			red=255
		final.append(str(red)+' '+str(red)+' '+str(red)+'\n')
		#count+=1
	return ''.join(final)

def main(argv):
	o=openfile(argv)
	orig=[]
	for line in o:
		orig.append(line.split())
	wid=int(orig[1][0])
	hei=int(orig[1][1])
	print str(wid)
	print str(hei)
	orig_c=orig_colors(orig)
	with open('hidden.ppm','w') as fin:
		print >> fin, 'P3\n'+str(wid)+' '+str(hei)+'\n'+'255\n'
		print >> fin, decode(orig_c)
	o.close()

if __name__=='__main__':
	main(sys.argv)