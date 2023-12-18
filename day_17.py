from utils.all import *


def list2grid(l: list) -> dict:
    return {(x, y): l[x][y] for x in range(len(l)) for y in range(len(l[0]))}


input_17 = read_input_line(17, sep="\n")
input_17 = read_input_line("test_17", sep="\n")
input_17 = mapl(lambda x: list(int(y) for y in x), input_17)
start = (0, 0)
end = (len(input_17) - 1, len(input_17[0]) - 1)

G = list2grid(input_17)
visit = deque([start])

print(start, end)
