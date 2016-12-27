import sys
from groups import *

def openfile(argv):
	try:
		f=open(argv[1])
		return f
	except:
		print 'Please enter a valid file name.'
		exit(1)

def read_values(file):
	contents_list=[]
	for line in file:
		contents_list.append(line.split())
	contents=[]
	for i in contents_list:
		for j in range(len(i)):
			contents.append(i[j])
	return contents

def read_colors(values):
	color_vals=values[4:len(values)]
	return groups_of_3(color_vals)

def make_list(colors,wid,hei):
	final=[]
	for y in range(hei):
		inner=[]
		for x in range(wid):
			pixel=(y*wid)+x
			inner.append(colors[pixel])
		final.append(inner)
	return final

def find_reach(argv):
	if len(argv)>=3:
		return int(argv[2])
	else:
		return 4

def calc_color(x,y,pixel_list,reach,wid,hei):
	min_x = x-reach
	if min_x < 0:
		min_x = 0
	max_x = x+reach
	if max_x >= wid:
		max_x = wid-1
	min_y = y-reach
	if min_y < 0:
		min_y = 0
	max_y = y+reach
	if max_y >= hei:
		max_y = hei-1
	r_tot=0
	g_tot=0
	b_tot=0
	tot=0
	for y in range(min_y,max_y+1):
		for x in range(min_x,max_x+1):
			r_tot+=int(pixel_list[y][x][0])
			g_tot+=int(pixel_list[y][x][1])
			b_tot+=int(pixel_list[y][x][2])
			tot+=1
	return [(r_tot/tot),(g_tot/tot),(b_tot/tot)]

def blur_image(pixel_list,reach,wid,hei):
	final=[]
	for y in range(len(pixel_list)):
		for x in range(len(pixel_list[0])):
			color=calc_color(x,y,pixel_list,reach,wid,hei)
			final.append(str(color[0]))
			final.append(' ')
			final.append(str(color[1]))
			final.append(' ')
			final.append(str(color[2]))
			final.append('\n')
	return ''.join(final)

def main(argv):
	o=openfile(argv)
	values=read_values(o)
	wid=int(values[1])
	hei=int(values[2])
	colors=read_colors(values)
	pixel_list=make_list(colors,wid,hei)
	neighbor_reach=find_reach(argv)
	with open('blurred.ppm','w') as fin:
		print >> fin, 'P3\n'+str(wid)+' '+str(hei)+'\n'+'255\n'
		print >> fin, blur_image(pixel_list,neighbor_reach,wid,hei)
	o.close()

if __name__ == '__main__':
	main(sys.argv)