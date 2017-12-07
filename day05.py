import numpy as np


def is_outside(array, idx):
    return idx < 0 or idx >= len(array)


def count_jumps(array):
    idx = 0
    jumps = 0
    while not is_outside(array, idx):
        array[idx] += 1
        idx += array[idx] - 1
        jumps += 1
    return jumps

def count_jumps_with_decrease(array):
    idx = 0
    jumps = 0
    while not is_outside(array, idx):
        move = -1 if array[idx] >= 3 else 1
        array[idx] += move
        idx += array[idx] - move
        jumps += 1
        # print(array)
    return jumps



array = np.loadtxt('data/day05_input.txt', dtype=int)
# array = [0,3,0, 1, -3]

print(count_jumps_with_decrease(array))


