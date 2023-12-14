from utils.all import *

input_14 = read_input_line(14, sep="\n")
#  input_14 = read_input_line("test_14", sep="\n")
input_14 = mapl(list, input_14)


cols = mapl(list, transpose(input_14))


def tilt_plus(cols: list) -> list:
    for i, row in enumerate(cols):
        for j, char in enumerate(row):
            if char == "O":
                cols[i][j] = "."
                for ni in autorange(j, len(row) - 1):
                    if ni == 0:
                        cols[i][0] = "O"
                    if cols[i][ni - 1] in "#O":
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

#  dish = input_14
#  #  for i in range(1_000_000_000):
#  for i in range(1):
#      print(i)
#      dish = mapl(list, transpose(dish))
#      dish = tilt_min(dish) #NORTH
#      dish = mapl(list, transpose(dish))
#      dish = tilt_plus(dish) #WEST
#      dish = mapl(list, transpose(dish))
#      dish = tilt_plus(dish) #SOUTH
#      dish = mapl(list, transpose(dish))
#      dish = tilt_min(dish) #EAST
#
#  for r in dish:
#      for ch in r:
#          print(ch,end="")
#      print()
#
#  tot = 0
#  for i, row in enumerate(dish):
#      for j, char in enumerate(row):
#          if char == "O":
#              tot += len(transformed) - i
#
#  print("Part Two:", tot)
#
