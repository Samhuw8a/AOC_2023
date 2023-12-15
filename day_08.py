from utils.all import *
from itertools import cycle

input_8 = read_input_line(8, sep="\n\n")
#  input_8 = read_input_line("test_08_part_2", sep="\n\n")

instructions, rdirections = input_8
ldirections = parse_multiline_string(rdirections, sep="\n")

directions = {
    x.split("=")[0].strip(): x.split("=")[1].strip().strip("())").split(", ")
    for x in ldirections
}

# Part One
cur = "AAA"
i = 0
instruction = cycle(instructions)
while not "ZZZ" == cur:
    inst = next(instruction)
    neighbors = directions[cur]
    i += 1
    if inst == "R":
        cur = neighbors[1]
    elif inst == "L":
        cur = neighbors[0]
    else:
        print("Error instruction is not Correct")
        break
print("Part_One:", i)

starts = filterl(lambda x: x[2] == "A", directions.keys())
instruction = cycle(instructions)
steps = []

for cur in starts:
    i = 0
    while not "Z" == cur[2]:
        inst = next(instruction)
        neighbors = directions[cur]
        i += 1
        if inst == "R":
            cur = neighbors[1]
        elif inst == "L":
            cur = neighbors[0]
        else:
            print("Error instruction is not Correct")
            break
    steps.append(i)

print("Part Two:", lcm(*steps))
