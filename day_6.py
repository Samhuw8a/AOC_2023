from utils.all import *


def distance(h: int, t: int) -> int:
    return h * (t - h)


input_6 = read_input_line(6, sep="\n")
#  input_6 = read_input_line("test_06", sep="\n")


def part_one() -> None:
    times = integers(input_6[0].split(":")[1])
    distances = integers(input_6[1].split(":")[1])

    tot = []
    for t, d in zip(times, distances):
        num = 0
        for i in range(1, t):
            if distance(i, t) > d:
                num += 1
        tot.append(num)

    print("Part One:", prod(tot))


def part_two() -> None:
    input_6_2 = read_input_line("06_2", sep="\n")
    #  input_6_2 = read_input_line("test_06_2", sep="\n")

    t = integers(input_6_2[0].split(":")[1])[0]  # type:ignore
    d = integers(input_6_2[1].split(":")[1])[0]  # type:ignore
    num = 0
    for i in range(1, t):
        if distance(i, t) > d:
            num += 1
    print("Part Two:", num)


part_one()
part_two()
