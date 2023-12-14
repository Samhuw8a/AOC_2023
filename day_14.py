from utils.all import *

input_14 = read_input_line(14, sep="\n")
#  input_14 = read_input_line("test_14", sep="\n")
input_14 = mapl(list, input_14)


cols = mapl(list, transpose(input_14))


def print_m(m: list) -> None:
    for i in m:
        for c in i:
            print(c, end="")
        print()


def tilt_plus(cols: list) -> list:
    for i, row in enumerate(cols):
        for x, char in enumerate(reversed(row)):
            j = len(row) - x - 1
            if char == "O":
                cols[i][j] = "."
                for ni in range(j, len(row)):
                    if ni == len(row) - 1:
                        cols[i][-1] = "O"
                        break
                    if cols[i][ni + 1] in "#O":
                        cols[i][ni] = "O"
                        break
    return cols


def tilt_min(cols: list) -> list:
    for i, row in enumerate(cols):
        for j, char in enumerate(row):
            if char == "O":
                cols[i][j] = "."
                for ni in autorange(j, 0):
                    if ni == 0:
                        cols[i][0] = "O"
                    if cols[i][ni - 1] in "#O":
                        cols[i][ni] = "O"
                        break
    return cols


cols = tilt_min(cols)
transformed = transpose(cols)
tot = 0
for i, row in enumerate(transformed):
    for j, char in enumerate(row):
        if char == "O":
            tot += len(transformed) - i

print("Part One:", tot)


def cycle(matrix: list) -> list:
    matrix = mapl(list, transpose(matrix))
    matrix = tilt_min(matrix)  # NORTH
    matrix = mapl(list, transpose(matrix))
    #  print_m(matrix)
    #  print()
    matrix = tilt_min(matrix)  # WEST
    #  print_m(matrix)
    #  print()
    matrix = mapl(list, transpose(matrix))
    matrix = tilt_plus(matrix)  # SOUTH
    matrix = mapl(list, transpose(matrix))
    #  print_m(matrix)
    #  print()
    matrix = tilt_plus(matrix)  # EAST
    return matrix


#  print_m(input_14)
#  print("--"*7)
#  west = cycle(input_14)
#  print_m(west)

dish = input_14
seen: dict = {mapt(tuple, dish): 0}
cur = 0
while cur <= 1_000_000_000:
    dish = cycle(dish)
    if mapt(tuple, dish) in seen:
        print_m(dish)
        of = seen[mapt(tuple, dish)]
        #  d = cur - seen[mapt(tuple, dish)]
        d = cur - of + 1
        dm = (1_000_000_000 - of) % d
        break
    cur += 1
    seen[mapt(tuple, dish)] = cur

print()
print_m(dish)
for _ in range(dm):
    dish = cycle(dish)

print(d)
print_m(dish)

tot = 0
for i, row in enumerate(dish):
    for j, char in enumerate(row):
        if char == "O":
            tot += len(transformed) - i

print("Part Two:", tot)
