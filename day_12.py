from utils.all import *

#  input_12 = read_input_line(12,sep="\n")
input_12 = read_input_line("test_12", sep="\n")
input_12 = mapt(lambda x: (x.split(" ")[0], integers(x)), input_12)


def parse_block(block: str, nums: tuple) -> int:
    if len(nums) == 1:
        if block[0] == "#" or block[-1] == "#":
            # '#??' or '????#'
            return 1
        if not block.find("#"):
            #'?????'
            return len(block) - nums[0] + 1
        if block.find("#"):
            NotImplemented
    elif len(nums) > 1:
        NotImplemented
    raise Exception("Block konnte nicht geparsed werdep")


def parse_row(data: tuple) -> int:
    row, groups = data
    return sum(groups)


print(input_12)

ans = mapl(parse_row, input_12)
print(ans)
print(sum(ans))
