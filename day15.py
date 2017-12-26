import os


def count_matching(a, b):
    sum = 0
    for i in range(40000000):
        a, b = produce_next_pair(a, b)
        sum += bin(a)[-16:] == bin(b)[-16:]

    return sum


def produce_next_pair(a,b):
    a_const = 16807
    b_const = 48271
    div = 2147483647

    return a*a_const % div, b*b_const % div


def gen_list(prev, const, mod):
    prev = prev*const % 2147483647
    while prev % mod > 0:
        prev = prev*const % 2147483647
    return prev


def count_matching_2(a, b):
    sum = 0
    for i in range(5000000):
        a = gen_list(a, 16807, 4)
        b = gen_list(b, 48271, 8)
        sum += bin(a)[-16:] == bin(b)[-16:]
    return sum

with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    data = [int(line.split()[4]) for line in file]


# print(count_matching(*data))
print(count_matching_2(*data))