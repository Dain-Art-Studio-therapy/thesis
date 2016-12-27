def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)


def open_file(file, type):
    try:
        f = open(file, type)
        return f
    except:
        print "The file could not be opened."
        exit(1)