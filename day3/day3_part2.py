import pathlib
import os

parent_dir = pathlib.Path(__file__).parent.resolve()
f = open(os.path.join(parent_dir, "day3_input.txt"), "r")


def find_common(triple):
    for i in triple[0]:
        for j in triple[1]:
            for k in triple[2]:
                if i == j and j == k:
                    return i


def find_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


total = 0

lines = f.read().splitlines()
for triple in [lines[i:i+3] for i in range(0, len(lines), 3)]:
    common = find_common(triple)
    priority = find_priority(common)
    print(f"Value: {common}, priority: {priority}")
    total += priority

print(total)
