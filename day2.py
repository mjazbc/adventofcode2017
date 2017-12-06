import numpy as np
from itertools import combinations

m = np.loadtxt('data/day2_input.txt', dtype=int)


def checksum1(m):
    return sum(np.max(m, 1) - np.min(m, 1))


def checksum2(m):
    for line in m:
        for a, b in combinations(line, 2):
            if a % b == 0:
                sum += a/b
            elif b % a == 0:
                sum += b/a
    return sum


print(checksum1(m))
print(checksum2(m))



