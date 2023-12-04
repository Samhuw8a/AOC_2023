from helpers import *
from collections import defaultdict
from typing import Any

input_4 = read_input_line(4, sep="\n")
#  input_4 = read_input_line("test_04", sep="\n")


def part_one() -> None:
    tot = 0

    for line in input_4:
        raw_nums = line.split(":")[1]
        nums = raw_nums.split("|")
        winning = integers(nums[0])
        given = list(set(integers(nums[1])))
        found = 0
        for num in given:
            if num in winning:
                found += 1
        if found:
            points = 2 ** (found - 1)
        else:
            points = 0
        #  print(found, points)
        tot += points

    print("Part One:", tot)


def part_two() -> None:
    cards = []
    for index, line in enumerate(input_4):
        raw_nums = line.split(":")[1]
        nums = raw_nums.split("|")
        winning = integers(nums[0])
        given = list(set(integers(nums[1])))
        found = 0
        for num in given:
            if num in winning:
                found += 1
        if found:
            points = 2 ** (found - 1)
            gained: tuple = tuple(index + i + 1 for i in range(found))
        else:
            points = 0
        cards.append((found, gained, index))
        gained: tuple = tuple()  # type:ignore

    games: Any = defaultdict(int)

    for game in cards:
        found = game[0]
        gained = game[1]
        index = game[2]
        games[index] += 1
        for n in gained:
            games[n] += games[index]
        #  print(games)

    #  print(games)
    print("Part Two:", sum(games.values()))


part_one()
part_two()
