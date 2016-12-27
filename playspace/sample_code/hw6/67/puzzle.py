import sys

def open_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
        exit(1)

def groups_of_3(nums):
    newlist = []
    for i in range(0, len(nums), 3):
        temp = nums[i:i+3]
        newlist.append(temp)
    return newlist

def process(f, hidden):
    # process each line of pixels
    n = f.read().split()
    p3 = n[0]
    width = (n[1])
    height = (n[2])
    max_col = (n[3])
    newlist = []
    for i in range(4, len(n)):
        newlist.append(int(n[i]))        
    num_list = groups_of_3(newlist)
    out(width, height, max_col, hidden, num_list)


def out(width, height, max_col, hidden, num_list):
    hidden.write('P3\n')
    hidden.write(width + ' ' + height + '\n' + max_col +'\n')
    final_list = []
    for i in num_list:
        col = i[0] * 10
        n = str(col)
        if (col > 255):
            hidden.write('255 255 255 ')
        else:
            hidden.write(n + ' ' + n + ' ' + n + ' ')

def main(argv):
    if len(argv) != 2:
        print >> sys.stderr, 'File not chosen.'
        exit(1)
    with open_file(argv[1], 'rb') as f:
        with open_file('hidden.ppm', 'wb') as hidden:
            process(f, hidden)


if __name__ == "__main__":
    main(sys.argv)
