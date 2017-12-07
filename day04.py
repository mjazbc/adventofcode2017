from collections import Counter

file = open('data/day04_input.txt', 'r')


def count_valid(file):
    sum = 0
    for line in file:
        sum += all(count == 1 for (word, count) in Counter(line.split()).items())
    return sum


def count_valid_anagrams(file):
    sum = 0
    for line in file:
        sum += all(count == 1 for (word, count) in Counter((''.join(sorted(word)) for word in line.split())).items())
    return sum


# print(count_valid(file))
print(count_valid_anagrams(file))
