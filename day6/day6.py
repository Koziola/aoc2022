import pathlib
import os


def are_unique_characters(characters):
    print(characters)
    return len(set(characters)) == len(characters)


parent_dir = pathlib.Path(__file__).parent.resolve()
f = open(os.path.join(parent_dir, "day6_input.txt"), "r")

line = f.read()

# start at the 15th character
for idx in range(15, len(line) - 1):
    characters = line[idx-14:idx]

    if are_unique_characters(characters):
        print(f"Found unique characters {characters}")
        print(idx)
        break
