import sys

def main(argv):
    f=try_open(argv[1],'r')
    blur=4
    if len(argv)>2:
       blur= int(argv[2])


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

    colorGrid= grid(groupedList,int(head2[0]),int(head2[1]))

    try_write(colorGrid,int(head2[0]),int(head2[1]),blur)
    f.close()


def groups_of_3(list):
    mainList=[]
    for n in range(0,len(list),3): 
       mainList.append(list[n:n+3])
          
    return mainList

def try_write(inputList,width,height,blur):
    output=try_open('blurred.ppm','w')

    output.write("P3"+"\n") 
    #How do we calculate width and height?
    output.write(str(width)+" "+str(height)+"\n")
    output.write("255"+ "\n") 
   
    #print RGB Values from grouped list
    for r in range(len(inputList)):
        #tracking row and column
        for c in range(len(inputList[r])):

            finpix=blur_pixel(inputList,c,r,blur)

            red=int(finpix[0])
            g=int(finpix[1])
            b=int(finpix[2])     

            output.write(str(red)+" "+str(g)+" "+str(b)+"\n")
    output.close()

   
def try_open(file,mode):
    try:
      newfile=open(file,mode)
      return newfile
    except:
      print "Cannot open file\n"
      print"Usage: Please enter filename only\n" 

def conv_list(inputList):
    intList=[]
    for e in range(len(inputList)):
       for f in range(len(inputList[e])):
            intList.append(int(inputList[e][f]))
    return intList

def blur_pixel(gridList,col,row,num):
    finpixel=[]
    rVal=0
    gVal=0
    bVal=0
    #value to divide by in order to get the average
    count=0
    for r in range((row-num),(row+num)):
       for c in range((col-num),(col+num)):
 	       try:
 	       	  rVal+=gridList[r][c][0]
 	       	  gVal+=gridList[r][c][1]
 	       	  bVal+=gridList[r][c][2]
 	       	  count+=1

 	       except: 
 	       	  count+=0
    avgR=rVal/count
    avgG=gVal/count
    avgB=bVal/count
    finpixel=[avgR,avgG,avgB]
    return finpixel

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
  
