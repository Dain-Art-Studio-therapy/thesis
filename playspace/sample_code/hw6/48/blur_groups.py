from blur_data import *


def groups_of_3(a_list):
    list_of_three = []
    if len(a_list) % 3 == 0:
        in_count = 0
        for i in range(len(a_list)/3):
            list_of_three.append([a_list[in_count], a_list[in_count+1], a_list[in_count+2]])
            in_count += 3
    elif len(a_list) % 3 == 1:
        in_count = 0
        for i in range(len(a_list)/3):
            list_of_three.append([a_list[in_count], a_list[in_count+1], a_list[in_count+2]])
            in_count += 3
        list_of_three.append([a_list[-1]])
    else:
        in_count = 0
        for i in range(len(a_list)/3):
            list_of_three.append([a_list[in_count], a_list[in_count+1], a_list[in_count+2]])
            in_count += 3
        list_of_three.append([a_list[-2], a_list[-1]])
    return list_of_three