__author__ = 'Jarrett'

def groups_of_three(list):
    newlist = []
    sublist = []

    for i in range(len(list)):
        if (i == (len(list) - 1)):
            sublist.append(list[i])
            newlist.append(sublist)
            return newlist

        elif (((i + 1) % 3) == 0):
            sublist.append(list[i])
            newlist.append(sublist)
            sublist = []


        else:
            sublist.append(list[i])