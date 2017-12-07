import math
import numpy as np

def create_matrix_spiral(input):
    dim = math.ceil(math.sqrt(input)) + 1
    m = np.zeros((dim, dim))
    x = math.floor(dim / 2)
    y = x
    m[y, x] = 1
    max = [x, x, x, x]
    i = 2
    while i <= input:
        while x <= max[0] and i <= input:
            x += 1
            m[y, x] = i
            i += 1
        max[0] = x

        while y >= max[1] and i <= input:
            y -= 1
            m[y, x] = i
            i += 1
        max[1] = y

        while x >= max[2] and i <= input:
            x -= 1
            m[y, x] = i
            i += 1
        max[2] = x

        while y <= max[3] and i <= input:
            y += 1
            m[y, x] = i
            i += 1
        max[3] = y

    return m, (y, x)

def create_matrix_sums(input):
    dim = math.ceil(math.sqrt(input)) + 1
    m = np.zeros((dim, dim))
    x = math.floor(dim / 2)
    y = x
    m[y, x] = 1
    max = [x, x, x, x]
    i = 2
    while i <= input:
        while x <= max[0] and i <= input:
            x += 1
            i = np.sum(neighbours(m, x, y))
            m[y, x] = i
        max[0] = x

        while y >= max[1] and i <= input:
            y -= 1
            i = np.sum(neighbours(m, x, y))
            m[y, x] = i
        max[1] = y

        while x >= max[2] and i <= input:
            x -= 1
            i = np.sum(neighbours(m, x, y))
            m[y, x] = i
        max[2] = x

        while y <= max[3] and i <= input:
            y += 1
            i = np.sum(neighbours(m,x,y))
            m[y, x] = i
        max[3] = y

    return m, i


def neighbours(m, x, y):
    return m[y-1 : y+2, x-1 : x+2]


def manhattan_to_center(input, x, y):
    dim = math.floor(math.ceil(math.sqrt(input))/2)
    return abs(x-dim) + abs(y-dim)


input = 289326
# m, (y,x) = create_matrix_spiral(input)

m, x = create_matrix_sums(input)

print(x)
print(m)
# print(manhattan_to_center(input, x, y))
