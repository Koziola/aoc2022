import pathlib
import os

parent_dir = pathlib.Path(__file__).parent.resolve()
f = open(os.path.join(parent_dir, "day4_input.txt"), "r")


def contains_other_total(self, other):
    return self[0] <= other[0] and self[1] >= other[1]


def contains_other_partial(self, other):
    return (self[0] <= other[0] and self[1] >= other[0]) or (self[0] <= other[1] and self[1] >= other[1])


total = 0
for line in f.read().splitlines():
    assignments = line.split(",")
    pair_a = list(map(lambda x: int(x), assignments[0].split("-")))
    pair_b = list(map(lambda x: int(x), assignments[1].split("-")))

    # part 1
    # if contains_other_total(pair_a, pair_b) or contains_other_total(pair_b, pair_a):
        # total += 1

    # part 2
    if contains_other_partial(pair_a, pair_b) or contains_other_partial(pair_b, pair_a):
        total += 1


print(total)
