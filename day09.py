import os

with open('data/'+os.path.basename(__file__).rstrip('.py')+'_input.txt', 'r') as file:
    data = file.read()


def score(data):
    cancel = False
    garbage = False
    level = 0
    sum = 0
    sum_garbage = 0

    for c in data:
        if cancel:
            cancel = False
            continue
        elif c == '!':
            cancel = True
        elif c == '>':
            garbage = False
        elif garbage:
            sum_garbage = sum_garbage+1
            continue
        elif c == '<':
            garbage = True
        elif c == '{':
            level += 1
        elif c == '}':
            sum += level
            level -= 1
    return sum, sum_garbage


score_sum, garbage_sum = score(data)
print(score_sum)
print(garbage_sum)
