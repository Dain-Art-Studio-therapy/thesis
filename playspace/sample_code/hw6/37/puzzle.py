
import sys



def open_file(name,mode): 
    try: 
        return open(name,mode) 
    except IOError as e: 
        print >>sys.stderr, '{0}:{1}'.format(name,e.strerror) 
        exit(1) 


def groups_of_3(nums):
    threes = []
    for i in range(0,len(nums),3):
        threes.append(nums[i:i+3])
    return threes


def process_file(f):
    line_after_header = []
    for line in f:
        line_after_header.append(line)
    return line_after_header

def process_header(f):
    head = [next(f) for x in xrange(3)]
    return head


def read(File):

    hidden = open('hidden.ppm','w')

    header = process_header(File)
    for line in header:
        hidden.write(line)
    
    lines_after_header = process_file(File)
    intLines = [int(i) for i in lines_after_header]
   

    pixel_list = groups_of_3(intLines)  

    for pixel in pixel_list:

        decoded_r = min(255,pixel[0]*10)
        decoded_g = min(255,pixel[0]*10)
        decoded_b = min(255,pixel[0]*10)

        hidden.write(str(int(decoded_r)) + ' ' 
                     + str(int(decoded_g)) + ' ' 
                     + str(int(decoded_b))+'\n')
        
    hidden.close()


def main(inFile):
    with open_file(inFile,'r') as f:

        read(f)
       






if __name__=='__main__':
    main(sys.argv[1])

