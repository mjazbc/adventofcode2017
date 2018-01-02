import time

def circular_buffer(step):
    buffer = []
    pos = 0
    for i in range(0, 2018):
        buffer.insert(pos, i)
        pos = (pos + step) % len(buffer) + 1

    return buffer[(buffer.index(2017) + 1) % len(buffer)]


def circular_buffer_idx(step, loops):
    value_after_zero = 0
    pos = 0
    for i in range(0, loops):
        if pos == 1:
            value_after_zero = i
        pos = (pos + step) % (i + 1) + 1

    return value_after_zero

step_size = 316

print(circular_buffer(step_size))
print(circular_buffer_idx(step_size, 50000001))