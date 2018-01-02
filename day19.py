import os

grid = []

with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.replace('\n', '')) + ([' '] * (201 - len(line))))


def move(dir, idx):
    if dir == 'D':
        idx = (idx[0] + 1, idx[1])
    elif dir == 'U':
        idx = (idx[0] - 1, idx[1])
    elif dir == 'L':
        idx = (idx[0], idx[1] - 1)
    elif dir == 'R':
        idx = (idx[0], idx[1] + 1)

    return idx


def change_dir(dir, idx, path):
    if dir == 'U' or dir == 'D':
        if len(path[idx[0]]) > idx[1] + 1 and path[idx[0]][idx[1] +1] == '-':
            return 'R'
        else:
            return 'L'
    else:
        if len(path) > idx[0] + 1 and path[idx[0] + 1][idx[1]] == '|':
            return 'D'
        else:
            return 'U'


def collect_letters(path):
    curr_idx = (0, path[0].index('|'))
    curr_dir = 'D'
    curr_el = '|'
    string = ''
    steps = 0

    while curr_el != ' ':

        if curr_el == '+':
            curr_dir = change_dir(curr_dir, curr_idx, path)

        if curr_el.isalpha():
            string += curr_el

        curr_idx = move(curr_dir, curr_idx)
        curr_el = path[curr_idx[0]][curr_idx[1]]

        steps += 1

    return string, steps

print(collect_letters(grid))
