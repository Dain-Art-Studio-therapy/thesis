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

def groups_of_width(nums, width):
    newlist = []
    w = int(width)
    for i in range(0, len(nums), w):
        temp = nums[i:i+w]
        newlist.append(temp)
    return newlist

def process(f, blurred, argv, reach):
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
    out(width, height, max_col, blurred, num_list, argv, reach)

def out(width, height, max_col, blurred, num_list, argv, reach):
    blurred.write('P3\n')
    blurred.write(width + ' ' + height + '\n' + max_col +'\n')
    two_d = groups_of_width(num_list, width)
    blur(argv, two_d, blurred, reach, width, height)

def calc(r, y, x, two_d, width, height, blurred):
    # height_of_box = (reach * 2) + 1 r = reach y = row, x = col
    w = int(width)
    h = int(height)
    start_y = y - r
    start_x = x - r
    end_y = y + r
    end_x = x + r
    if start_y <= 0:
        start_y = 0
    if start_x <= 0:
        start_x = 0
    if end_y >= h:
        end_y = h
    if end_x >= w:
        end_x = w
    count = 0
    r = 0
    g = 0
    b = 0
    for row in range(start_y, end_y):
        for col in range(start_x, end_x):
            count = count + 1
            r += two_d[row][col][0]
            g += two_d[row][col][1]
            b += two_d[row][col][2]
    r = str((r/count))
    g = str((g/count))
    b = str((b/count))
    blurred.write(r + ' ' + g + ' ' + b + ' ')

def blur(argv, two_d, blurred, reach, width, height):
    for i in range(len(two_d)):
        for j in range(len(two_d[i])):
            # gets i and a j
            calc(reach, i, j, two_d, width, height, blurred)

def check_arg(argv):
    if len(argv) == 1:
        print >> sys.stderr, 'File not chosen.'
        exit(1)
    if len(argv) == 2:
        blur = 4
        return blur
    if len(argv) == 3:
        blur = int(argv[2])
        return blur

def main(argv):
    reach = check_arg(argv)    
    with open_file(argv[1], 'rb') as f:
        with open_file('blurred.ppm', 'wb') as blurred:
            process(f, blurred, argv, reach)

if __name__ == "__main__":
    main(sys.argv)
