import os


def get_register_val(registers, reg):
    if reg.isdigit():
        return int(reg)
    if reg not in registers:
        registers[reg] = 0

    return registers[reg]


def run(data):
    pos = 0
    registers = dict()
    last_freq = 0

    while len(data) > pos >= 0:

        cmd, reg, val = data[pos].split() if len(data[pos].split()) > 2 else data[pos].split() + ['']
        reg_val = get_register_val(registers, reg)

        if not val.replace('-', '').isdigit():
            val = get_register_val(registers, val)

        val = int(val)
        if cmd == 'set':
            registers[reg] = val
        elif cmd == 'sub':
            registers[reg] = reg_val - val
        elif cmd == 'add':
            registers[reg] = reg_val + val
        elif cmd == 'mul':
            registers[reg] = reg_val * val
        elif cmd == 'mod':
            registers[reg] = reg_val % val
        elif cmd == 'jgz' and reg_val > 0:
            pos += val - 1
        elif cmd == 'snd' and reg_val:
            last_freq = reg_val
        elif cmd == 'rcv' and reg_val:
            return last_freq

        pos += 1
    pass


def run_command(data, registers, pos, msgq_snd, msgq_rcv):

    if pos >= len(data):
        return pos, 0, True

    terminated = False
    cmd, reg, val = data[pos].split() if len(data[pos].split()) > 2 else data[pos].split() + ['']
    reg_val = get_register_val(registers, reg)

    if not val.replace('-', '').isdigit():
        val = get_register_val(registers, val)

    val = int(val)
    if cmd == 'set':
        registers[reg] = val
    elif cmd == 'sub':
        registers[reg] = reg_val - val
    elif cmd == 'add':
        registers[reg] = reg_val + val
    elif cmd == 'mul':
        registers[reg] = reg_val * val
    elif cmd == 'mod':
        registers[reg] = reg_val % val
    elif cmd == 'jgz' and reg_val > 0:
        pos += val - 1
    elif cmd == 'snd':
        msgq_snd.insert(0, registers[reg])
    elif cmd == 'rcv':
        if msgq_rcv:
            registers[reg] = msgq_rcv.pop()
        else:
            terminated = True
            pos -= 1

    return pos + 1, cmd == 'snd', terminated


def run_threads(data):
    reg0, reg1 = {'p': 0}, {'p': 1}
    pos0, pos1 = 0, 0
    msg_q0, msg_q1 = [], []
    send_count = 0
    term0, term1 = False, False

    while not (term0 and term1):
        pos0, _, term0 = run_command(data, reg0, pos0, msg_q1, msg_q0)
        pos1, tmp, term1 = run_command(data, reg1, pos1, msg_q0, msg_q1)
        send_count += tmp

    return send_count


with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]


print(run(data))
print(run_threads(data))
