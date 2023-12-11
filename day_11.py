from utils.all import *


def btwn(x: int, src: int, dst: int) -> bool:
    return dst < x < src or src < x < dst


input_11 = read_input_line(11, sep="\n")
#  input_11 = read_input_line("test_11", sep="\n")
input_11 = mapl(list, input_11)

row_insertions = []
for i, row in enumerate(input_11):
    if all(x == "." for x in row):
        row_insertions.append(i)

trow = transpose(input_11)

col_insertions = []
for i, row in enumerate(trow):
    if all(x == "." for x in row):
        col_insertions.append(i)

G = graph_from_grid(input_11, "#", ".", True)
ks = list(G.keys())

# Part One
#  OFFSET = 999999

# Part Two
OFFSET = 1


def dist(src: tuple, dst: tuple) -> int:
    nx = len(filterl(lambda x: btwn(x, src[1], dst[1]), col_insertions))
    dx = abs(src[1] - dst[1]) + nx * OFFSET
    ny = len(filterl(lambda x: btwn(x, src[0], dst[0]), row_insertions))
    dy = abs(src[0] - dst[0]) + ny * OFFSET
    return dx + dy


tot = 0
for i, src in enumerate(ks):
    for dst in ks[i + 1 :]:
        tot += dist(src, dst)

print("Answer:", tot)
