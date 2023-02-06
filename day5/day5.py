import pathlib
import os
import re

parent_dir = pathlib.Path(__file__).parent.resolve()
f = open(os.path.join(parent_dir, "day5_input.txt"), "r")


def parse_setup(setup):
    queues = []

    # reverse the text to build the list of queues, then skip the first row
    rev = setup.split("\n")[::-1][1:]

    for line in rev:
        idx = 1
        queue_idx = 0
        while idx < len(line):
            if queue_idx > len(queues) - 1:
                queues.append([])

            current = line[idx]

            if current.isalpha():
                current_queue = queues[queue_idx]
                current_queue.append(current)
            queue_idx += 1
            idx += 4

    return queues


def parse_instruction(instruction):
    print(f"instruction: {instruction}")
    numbers = re.findall(r"\d+", instruction)
    print(len(numbers))
    if len(numbers) != 3:
        raise ValueError("AOC lied or we messed up parsing instructions")

    return list(map(lambda x: int(x), numbers))


setup, instructions = f.read().split("\n\n")

queues = parse_setup(setup)

for instruction in instructions.split("\n"):
    if not instruction.strip():
        continue

    quantity, src, dst = parse_instruction(instruction)
    print(quantity, src, dst)

    src_queue = queues[src - 1]
    dst_queue = queues[dst - 1]

    crane = src_queue[-quantity:]
    del src_queue[-quantity:]
    dst_queue.extend(crane)

    # part 1
    # for i in range(quantity):
        # crate = src_queue.pop()
        # dst_queue.append(crate)


result = ""
for queue in queues:
    result += queue[-1]
print(result)
