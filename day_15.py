from utils.all import *

input_15 = read_input_line(15, sep=",")
#  input_15 = read_input_line("test_15",sep=",")


def hash_string(string: str) -> int:
    cur = 0
    for c in string:
        cur += ord(c)
        cur = cur * 17
        cur = cur % 256
    return cur


input_15 = mapl(hash_string, input_15)
print(input_15)
ans = sum(input_15)
print("Part One:", ans)
