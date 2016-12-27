def find_addresses(center, reach):

    addresses = []
    
    for i in range(reach*2 + 1):
        for j in range(reach*2 + 1):
            addresses.append((
                center[0]-reach + i,
                center[1]-reach + j
                ))

    return addresses


def find_neighbors(rolodex, addresses):

    neighbors = []
    
    for address in addresses:
        for entry in rolodex:
            if address == entry[1]:
                neighbors.append(entry[0])

    return neighbors


def locate(pindex, width):

    for i in range(width):
        if pindex < width * (i+1):
            col = pindex - width*i
            row = i
            return col, row


def get_locations(pixel_list, width):

    locations = []

    for i in range(len(pixel_list)):
        locations.append(locate(i, width))

    return locations


def average(pixels):

    r = 0
    g = 0
    b = 0
    total = 0

    for pixel in pixels:
        total += 1
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]

    r_avg = r // total
    g_avg = g // total
    b_avg = b // total

    return r_avg, g_avg, b_avg 


def get_rolodex(pixels, width):

    rolodex = []
    locations = get_locations(pixels, width)
    for i in range(len(pixels)):
        rolodex.append((pixels[i], locations[i]))
    return rolodex


def find_neighbors(rolodex, addresses):

    neighbors = []
    
    for entry in rolodex:
        for address in addresses:
            if address in entry:
                neighbors.append(entry[0])

    return neighbors


def blur(pixels, width, reach):

    new_pixels = []

    rolodex = get_rolodex(pixels, width)

    for i in range(len(pixels)):
        center = locate(i, width)
        addresses = find_addresses(center, reach)
        neighbors = find_neighbors(rolodex, addresses)
        new_pixels.append(average(neighbors))
        
    return new_pixels


