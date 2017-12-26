import os

with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = {int(line.split(' <-> ')[0]): list(map(int, line.split(' <-> ')[1].split(', '))) for line in file}


def detect_group(curr, visited):
    if curr in visited:
        return visited

    visited.append(curr)
    for x in data[curr]:
        detect_group(x, visited)

    return visited


def count_groups():
    return len({tuple((sorted(detect_group(p, [])))) for p in data})


print(len(detect_group(0,[])))
print(count_groups())