import pathlib
import os

parent_dir = pathlib.Path(__file__).parent.resolve()
f = open(os.path.join(parent_dir, "day3_input.txt"), "r")


def find_common(line):
    seen = set({})
    for i in first:
        if i in seen:
            continue
        for j in second:
            if i == j:
                return i
        seen.add(i)


def find_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


total = 0
for line in f.read().splitlines():
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]
    common = find_common(first, second)
    priority = find_priority(common)
    print(f"Value: {common}, priority: {priority}")
    total += priority

print(total)

