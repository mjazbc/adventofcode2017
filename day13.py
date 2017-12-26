import os

def get_scanner_pos(rng, step):
    return (list(range(0, rng-1)) + list(range(rng-1, 0, -1)))[step % ((rng-1) * 2)]


def severity(data):
    return sum([(get_scanner_pos(r, s) == 0) * s * r for s, r in data.items()])


def free_pass(data, delay):
    return all([get_scanner_pos(r, s + delay) for s, r in data.items()])


def calc_delay(data):
    delay = 0
    while not free_pass(data, delay):
        delay += 1
    return delay


with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = {int(line.split(':')[0]) : int(line.split(':')[1]) for line in file}

print(severity(data))
print(calc_delay(data))
