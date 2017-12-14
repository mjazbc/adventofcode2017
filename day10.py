import os
from functools import reduce


def reverse_sublist(start_idx, sub_length, data):
    end_idx = sub_length + start_idx - 1
    while end_idx > start_idx:
        data[start_idx % len(data)], data[end_idx % len(data)] = data[end_idx % len(data)], data[start_idx % len(data)]
        end_idx -= 1
        start_idx += 1


def knot(data):
    pos, skip_size = 0, 0
    numbers = list(range(0, 256))
    for length in data:
        reverse_sublist(pos, length, numbers)
        pos += length + skip_size
        skip_size += 1
    return numbers[0] * numbers[1], numbers


def hash(data):
    data = (data + [17, 31, 73, 47, 23])*64
    _, data = knot(data)
    bits = [reduce(lambda x, y: x ^ y, data[i:i + 16]) for i in range(0, len(data), 16)]
    hex_data = ''.join(['%02x' % bit for bit in bits])
    return hex_data



with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = file.read()

int_data = list(map(int, data.split(',')))
byte_data = list(map(lambda x : int(ord(x)), data))

knot_res, _ = knot(int_data)
print(knot_res)
print(hash(byte_data))
