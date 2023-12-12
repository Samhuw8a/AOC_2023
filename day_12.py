from utils.all import *

input_12 = read_input_line(12, sep="\n")
#  input_12 = read_input_line("test_12", sep="\n")
input_12 = mapt(lambda x: (x.split(" ")[0], integers(x)), input_12)


def sliding_window(string: str, c: str, lenght: int) -> int:
    if lenght >= len(string):
        raise Exception("string lenght doesn't match the provided len")
    tot = 0
    for i in range(len(string) - lenght + 1):
        win = string[i : i + lenght]
        print(win)
        assert len(win) == lenght
        tot += "#" in win
    return tot


def ending_in(string: str, c: str) -> bool:
    start = not bool(string.lstrip(c).find(c))
    end = not bool(string.rstrip(c).find(c))
    return start or end


def parse_block(block: str, nums: tuple) -> int:
    if len(nums) == 1:
        if ending_in(block, "#"):
            # '#??' or '????#'
            return 1
        if not block.find("#"):
            # '?????'
            return len(block) - nums[0] + 1
        if block.find("#"):
            if len(block) == nums[0]:
                return 1
            return sliding_window(block, "#", nums[0])

    elif len(nums) > 1:
        NotImplemented
    raise Exception("Block konnte nicht geparsed werdep")


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
        tot += is_correct(nrow, groups)
    return tot


#  print(input_12)
#
ans = mapl(parse_row, input_12)
#  print(ans)
print("Part One:", sum(ans))
