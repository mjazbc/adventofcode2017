import numpy as np
import os

def matrix_to_string(m):
    return '/'.join([''.join(l) for l in m.tolist()])


def string_to_matrix(rule):
    return np.matrix([list(r) for r in rule.split('/')])


def flip_rotate_rules(rules):
    rules_rotated = dict()
    for rule, tran in rules.items():
        for i in range(0,4):
            m = np.rot90(string_to_matrix(rule), i)
            rules_rotated[matrix_to_string(m)] = tran
            rules_rotated[matrix_to_string(np.flip(m, 0))] = tran
            rules_rotated[matrix_to_string(np.flip(m, 1))] = tran
            rules_rotated[matrix_to_string(np.flip(np.flip(m, 0), 1))] = tran

    return rules_rotated


def enhance(m, n, rules):
    dim = (len(m) // n) * (n+1)
    new_m = np.array([], dtype=np.int64).reshape(0, dim)
    for i in range(0, len(m), n):
        new_row = np.array([], dtype=np.int64).reshape(n +1, 0)
        for j in range(0, len(m), n):
            new_row = np.hstack((new_row, string_to_matrix(rules[matrix_to_string(m[i:i+n, j:j+n])])))
        new_m = np.vstack((new_m, new_row ))

    return new_m


def iterate(rules, n, image):
    for i in range(n):
        print(i)
        if not len(image) % 2:
            image = enhance(image, 2, rules)
        elif not len(image) % 3:
            image = enhance(image, 3, rules)
        # print(image)

    return dict(zip(*np.unique(image.tolist(), return_counts=True)))['#']

rules = dict()
with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    for line in file.readlines():
        rule = line.split('=>')
        rules[rule[0].strip()] = rule[1].strip()

rules = flip_rotate_rules(rules)

initial_image = np.matrix([['.', '#', '.'],
                           ['.', '.', '#'],
                           ['#', '#', '#']])

print(iterate(rules, 5, initial_image))
print(iterate(rules, 18, initial_image))