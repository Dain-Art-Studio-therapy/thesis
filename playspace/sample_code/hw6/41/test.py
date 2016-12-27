__author__ = 'Jarrett'

import blur

def test_machine(num):
    testlist = []
    for i in range(num):
        n = str(i)
        testlist.append([n, n, n])
    return testlist

test4 = test_machine(400)
temp4 = blur.pixel_grid(test4, 20)
blur.blur(test4, 20, 20, 1)