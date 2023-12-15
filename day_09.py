from utils.all import *

lines = read_input_line(9, sep="\n")
#  lines = read_input_line("test_09", sep="\n")

nums = mapl(integers, lines)


def next_row(row: list) -> list:
    nrow: list = []
    for i in range(1, len(row)):
        nrow.append((row[i] - row[i - 1]))
    return nrow


def extrapolate(nums: list) -> int:
    if len(set(nums)) == 1:
        return nums[0]

    delta = extrapolate(next_row(nums))
    return nums[-1] + delta


def extrapolate_right(nums: list) -> int:
    if len(set(nums)) == 1:
        return nums[0]

    delta = extrapolate_right(next_row(nums))
    return nums[0] - delta


extrapolatedl = map(extrapolate, nums)
extrapolatedr = map(extrapolate_right, nums)
print("Part One:", sum(extrapolatedl))
print("Part Two:", sum(extrapolatedr))
