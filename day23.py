import os

with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]


def get_register_val(registers, reg):
    if reg not in registers:
        registers[reg] = 0

    return registers[reg]

def debug(data, initial_a):
    pos = 0
    mul_count = 0
    registers = {'a' : initial_a}
    while pos < len(data):
        cmd, reg, val = data[pos].split()

        if reg.replace('-','').isdigit():
            reg_val = int(reg)
        else:
            reg_val = get_register_val(registers, reg)

        if not val.replace('-', '').isdigit():
            val = get_register_val(registers, val)

        val = int(val)
        if cmd == 'set':
            registers[reg] = val
        elif cmd == 'sub':
            registers[reg] = reg_val - val
        elif cmd == 'mul':
            registers[reg] = reg_val * val
            mul_count += 1
        elif cmd == 'jnz' and reg_val:
            pos += val - 1

        if 'g' in registers:
            print('g',registers['g'])
        if 'h' in registers:
            print(registers['h'])
        pos += 1

    return mul_count

print(debug(data, 1))

