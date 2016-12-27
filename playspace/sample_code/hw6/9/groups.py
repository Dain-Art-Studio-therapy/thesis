

def groups_of_3(values):
    newlist = []
    for v in range(0, len(values), 3):
        newlist.append(values[v:v + 3])
    return newlist

