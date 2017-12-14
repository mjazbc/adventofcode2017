import os
import numpy as np


def dist(coords):
    return int(sum(abs(num) for num in coords))


def find_child(data):
    coords = np.zeros(2)
    max_dist = 0
    for direction in data:
        move = np.zeros(2)
        if 's' in direction:
            move[1] -= 1
        elif 'n' in direction:
            move[1] += 1
        if 'e' in direction:
            move[0] += 1
        elif 'w' in direction:
            move[0] -= 1

        move = move * 0.5 if len(direction) == 2 else move
        coords += move
        curr_dist = dist(coords)
        max_dist = curr_dist if curr_dist > max_dist else max_dist

    return dist(coords), max_dist


with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = file.read().split(',')

end, max = find_child(data)

print(end)
print(max)