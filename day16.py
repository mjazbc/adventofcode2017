import string
import os


def spin(data, num):
    return data[-num:] + data[0:16-num]


def exchange(data, a, b):
    a, b = int(a), int(b)
    data[a], data[b] = data[b], data[a]


def partner(data, a, b):
    exchange(data, data.index(a), data.index(b))


def dance(data, line):
    for inst in data:
        inst_c = inst[0]
        if inst_c == 's':
            line = spin(line, int(inst[1:]))
        elif inst_c == 'p':
            partner(line, *inst[1:].split('/'))
        elif inst_c == 'x':
            exchange(line, *inst[1:].split('/'))

    return line


def billion_dances(data, line):
    for i in range(1000000000 % 48):    # line gets back to initial position after 48 dances
        line = dance(data, line)

    return line


with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    data = file.read().split(',')

initial_line = list(string.ascii_lowercase[0:16])

print(''.join(dance(data, initial_line.copy())))
print(''.join(billion_dances(data, initial_line)))