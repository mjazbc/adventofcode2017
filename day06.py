import numpy as np


def distribute(idx, curr_array):
    val = curr_array[idx]
    curr_array[idx] = 0
    for i in range(idx +1, idx +val +1):
        curr_array[i % len(curr_array)] += 1
    return curr_array


def count_cycles(array):
    seen = []
    while not any((array == x).all() for x in seen):
        seen.append(array)
        array = distribute(np.argmax(array), np.copy(array))
    return len(seen), array


def count_loop_size(array):
    _, loop_start = count_cycles(array)
    array = distribute(np.argmax(loop_start), np.copy(loop_start))
    c = 1
    while not np.array_equal(loop_start, array):
        array = distribute(np.argmax(array), np.copy(array))
        c += 1
    return  c


array = np.loadtxt('data/day06_input.txt', dtype=int)

print(count_cycles(array)[0])
print(count_loop_size(array))

