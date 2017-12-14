import os

with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = [line.strip() for line in file]


def parse_condition(condition, register):

    reg_name, cond, value = condition.split()

    if reg_name not in register:
        register[reg_name] = 0

    if cond == '>=':
        return register[reg_name] >= int(value)
    elif cond == '<=':
        return register[reg_name] <= int(value)
    elif cond == '==':
        return register[reg_name] == int(value)
    elif cond == '!=':
        return register[reg_name] != int(value)
    elif cond == '>':
        return register[reg_name] > int(value)
    elif cond == '<':
        return register[reg_name] < int(value)


def parse_action(action):
    if 'inc' in action:
        reg_name, value = action.split('inc')
        const = 1
    else:
        reg_name, value = action.split('dec')
        const = -1

    return reg_name.strip(), int(value.strip()), const


def find_max(data):
    register = dict()
    max_ever = float('-inf')
    for line in data:
        action, condition = line.split('if')

        reg_name, val, const = parse_action(action)

        if reg_name not in register:
            register[reg_name] = 0

        condition_met = parse_condition(condition, register)

        if condition_met:
            register[reg_name] += (val * const)

        max_ever = max(register.values()) if max(register.values()) > max_ever else max_ever

    return max(register.values()), max_ever


max_end, max_ever = find_max(data)
print(max_end)
print(max_ever)
