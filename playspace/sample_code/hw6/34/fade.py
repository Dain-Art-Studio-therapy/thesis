import sys
import math

def main(argv):
    f=try_open(argv[1],'r')
    row=int(argv[2])
    col=int(argv[3])
    radius=float(argv[4])
    head1=f.readline().split()
    head2=f.readline().split()
    head3=f.readline().split()
    mergedList=[]

    for line in f:
        mergedList.append(line.split())
    
    #NEED TO PUT LIST OF LISTS INTO A INT LISTS
    int_list=conv_list(mergedList)
    #color values divided into list of three into a list
    groupedList=groups_of_3(int_list)

    #put pixels (grouped RGB values) into iterable grid
  
   
    #Set up the image for writing
    try_write(groupedList,int(head2[0]),int(head2[1]),radius,row,col)
    f.close()

def groups_of_3(list):
    mainList=[]
    for n in range(0,len(list),3): 
       mainList.append(list[n:n+3])
          
    return mainList

def try_write(inputList,width,height,radius,row,column):
    output=try_open('faded.ppm','w')

    output.write("P3"+"\n") 
    #How do we calculate width and height?
    output.write(str(width)+" "+str(height)+"\n")
    output.write("255"+ "\n") 
    c=0
    r=0
    #print RGB Values from grouped list
    for num in range(len(inputList)):
        #tracking row and column
        c+=1

        if c==width:
           c=0
           r+=1
        
        
        #compute dist
             
        dist=calc_dist(c,r,column,row)
        scale=(radius-dist)/float(radius)
    
        if scale < 0.2:
            scale=0.2
        

        red=int(inputList[num][0]*scale)
        g=int(inputList[num][1]*scale)
        b=int(inputList[num][2]*scale)

            

        output.write(str(red)+" "+str(g)+" "+str(b)+"\n")
    output.close()

def conv_list(inputList):
    intList=[]
    for e in range(len(inputList)):
       for f in range(len(inputList[e])):
            intList.append(int(inputList[e][f]))
    return intList
        


def try_open(file,mode):
    try:
      newfile=open(file,mode)
      return newfile
    except:
      print "Cannot open file\n"
      print"Usage: Please enter filename only\n"    

def calc_dist(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

def grid(inputlist, width, height):
    
    gridList=[]
    row=[]

    for n in range(0, len(inputlist), width):
        for i in range(n,n+width):
            row.append(inputlist[i])
        gridList.append(row)
        row=[]
    return gridList

if __name__== "__main__":
    main(sys.argv)
  
