def groups_of_three(list):
    new = []
    
    for index in range(len(list)/3):
        newer = []
        for i in range(3):
            newer.append(list[i + index * 3])
        new.append(newer)
    
    #for when list is not divisible by 3
    remainder = len(list) % 3
    var0 = len(list) - remainder
    var1 = len(list) - remainder + 1
    remainder_list = []
    if remainder == 2:
        remainder_list.append(list[var0])
        remainder_list.append(list[var1])
        new.append(remainder_list)
    elif remainder == 1:
        remainder_list.append(list[var0])
        new.append(remainder_list)
            
    return new
    
def open_file(file, type):
    try:
        f = open(file, type)
        return f
    except IOError as e:
        print "{0}: {1}".format(sys.argv[1], e.strerror)