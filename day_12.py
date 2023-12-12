from utils.all import *

#  input_12 = read_input_line(12, sep="\n")
input_12 = read_input_line("test_12", sep="\n")
input_12 = mapt(lambda x: (x.split(" ")[0], integers(x)), input_12)


def is_correct(string: str, nums: list) -> bool:
    blocks = filterl(bool, string.split("."))
    if len(blocks) != len(nums):
        return False
    return all(len(x) == y for x, y in zip(blocks, nums))


def parse_row(data: tuple) -> int:
    tot = 0
    row, groups = data
    for replace in product("#.", repeat=count_if(row, lambda x: x == "?")):
        nrow = row
        for c in replace:
            nrow = nrow.replace("?", c, 1)
            if count_if(nrow, lambda x: x == "#") > sum(groups):
                continue
        tot += is_correct(nrow, groups)
    return tot


def extract(data: tuple) -> tuple:
    row, groups = data
    nrow = "?".join([row] * 5)
    groups *= 5
    return (nrow, groups)


#  print(input_12)
#
ans = mapl(parse_row, input_12)
#  print(ans)
print("Part One:", sum(ans))

input_12 = mapl(extract, input_12)
print(parse_row(input_12[0]))
#  print(input_12)
#  ans = mapl(parse_row, input_12)
#  print(ans)
#  print("Part Two:", sum(ans))
