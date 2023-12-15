from helpers import *

games = read_input_line(2, sep="\n")
#  games = read_input_line("test_02", sep="\n")

max_cubes = {"red": 12, "green": 13, "blue": 14}

tot = 0
for game in games:
    seperated = game.split(":")
    id = int(seperated[0].split(" ")[1])
    rawhands = seperated[1].split(";")
    hands = mapl(lambda x: x.split(","), rawhands)
    hands = list(
        mapl(lambda x: (first_int(x.strip()), x.strip().split(" ")[1]), hand)
        for hand in hands
    )
    check = all(all(cube[0] <= max_cubes[cube[1]] for cube in round) for round in hands)
    #  print(check, game)
    tot += id * check


print("Part_one:", tot)

powers = 0
for game in games:
    rawhands = game.split(":")[1].split(";")
    hands = mapl(lambda x: x.split(","), rawhands)
    mins: dict = {"red": 0, "green": 0, "blue": 0}
    for round in hands:
        for cube in round:
            vals = cube.strip().split(" ")
            mins[vals[1]] = max(int(vals[0]), mins[vals[1]])
    power = mins["red"] * mins["blue"] * mins["green"]
    powers += power

print("Part_two", powers)
