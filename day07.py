import os
from collections import Counter

with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = [line for line in file]


def get_bottom(data):
    all_nodes = [line.split('->')[0].split()[0] for line in data]
    text = ''.join(data)
    return next(node for node in all_nodes if text.count(node) == 1)


def prepare_dicts(data):
    weights = dict()
    child_nodes = dict()
    for line in data:
        split = line.split('->')
        key = split[0].split()
        name = key[0].strip()
        weight = int(key[1].strip(' ()'))
        weights[name] = weight
        if len(split) > 1:
            child_nodes[name] = split[1].replace(' ', '').strip().split(',')
    return weights, child_nodes


def outlier_index(weights):
    for weight, count in Counter(weights).items():
        if count == 1:
            return weights.index(weight)


def get_weight(weights_dict, child_nodes_dict, node):
    if node not in child_nodes_dict:
        return weights_dict[node]

    weights = [get_weight(weights_dict, child_nodes_dict, child_node) for child_node in child_nodes_dict[node]]
    different_weights = list(set(weights))

    if len(set(weights)) > 1:  # A node with different weight was detected
        diff = abs(different_weights[0] - different_weights[1])  # calculate weight difference
        outlier_name = child_nodes_dict[node][outlier_index(weights)]
        print(weights_dict[outlier_name] - diff)  # print the solution
        weights[outlier_index(weights)] -= diff  # correct the wrong weight

    return sum(weights) + weights_dict[node]


bottom = get_bottom(data)
print(bottom)
weights, child_nodes = prepare_dicts(data)

get_weight(weights, child_nodes, bottom)

