# Nupur Garg

from sys import argv
import re


LEN_HEADER = 4


# Gets the file's contents.
def read_file(filename):
    fp = open(filename, 'r')
    text = fp.read()
    return [val for val in re.split(' |\n', text) if val]


def are_equal(num1, num2, epsilon=1):
    if isinstance(num1, int):
        return abs(num1 - num2) <= epsilon
    return num1 == num2


# Compares ppm files.
def compare_ppm(file1, file2):
    is_equal = True
    max_diff = 0

    for idx, items in enumerate(zip(file1, file2)):
        item1 = items[0]
        item2 = items[1]
        if idx >= LEN_HEADER:
            item1 = int(item1)
            item2 = int(item2)

        if not are_equal(item1, item2):
            is_equal = False
            max_diff = max(abs(item1 - item2), max_diff)
            if max_diff == 32:
                print('{0}\t{1}'.format(item1, item2))

    return is_equal, max_diff


def main():
    if len(argv) != 3:
        print('Usage: python3 compare.py [ ppm-file-1 ] [ ppm-file-2 ]')
        exit()

    file1 = read_file(argv[1])
    file2 = read_file(argv[2])
    is_equal, max_diff = compare_ppm(file1, file2)

    if is_equal:
        print('Congrats!')
    else:
        print('Keep working. Max diff {0}'.format(max_diff))


if __name__ == '__main__':
    main()

