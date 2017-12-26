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
    return numbers


def hash(data):
    data = (data + [17, 31, 73, 47, 23])*64
    data = knot(data)
    bits = [reduce(lambda x, y: x ^ y, data[i:i + 16]) for i in range(0, len(data), 16)]
    hex_data = ''.join(['%02x' % bit for bit in bits])
    return hex_data


def to_binary(string):
    return ''.join("{0:04b}".format(int(c, 16)) for c in string)


def count_zeros(data):
    sum_square = 0
    bit_data =[]
    for i in range(128):
        nums = list(map(lambda x: int(ord(x)), data+'-'+str(i)))
        bits = [i == '1' for i in to_binary(hash(nums))]
        bit_data += [bits]
        sum_square += sum(i == '1' for i in to_binary(hash(bits)))
    return sum_square, bit_data


def get_neighbors(row, column, data):
    neighbors = set()
    if row > 0 and data[row-1][column]:
        neighbors.add((row-1, column))
    if column > 0 and data[row][column-1]:
        neighbors.add((row, column - 1))

    return neighbors


def find_existing_group(i, j, groups_all):
    for ig, g in enumerate(groups_all):
        if (i, j) in g:
            return ig


def connect_regions(data):
    groups_all = []
    for i, row in enumerate(bit_grid):
        for j, column in enumerate(row):
            if column:
                neigh = get_neighbors(i, j, data)
                if neigh:
                    # find existing groups for neighbors. First create set to get rid of duplicates
                    existing = list({find_existing_group(*n, groups_all) for n in neigh})
                    # add current item to existing group of first neighbor
                    groups_all[existing[0]] = groups_all[existing[0]].union({(i, j)})
                    # if neighbors are in different groups, join them
                    if len(existing) == 2:
                        groups_all[existing[0]] = groups_all[existing[0]].union(groups_all[existing[1]])
                        groups_all.remove(groups_all[existing[1]])
                # if current item is not in any of the groups, create new one
                else:
                    groups_all.append({(i, j)})
    return len(groups_all)

data = 'jxqlasbh'

zeros, bit_grid = count_zeros(data)
print(zeros)
print(connect_regions(bit_grid))

