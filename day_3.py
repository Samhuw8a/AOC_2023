from helpers import *

input_3 = read_input_line(3, sep="\n")
#  input_3 = read_input_line("test_03", sep="\n")


def part_one() -> None:
    def is_symbol(char: str) -> bool:
        return char not in DIGITS and char != "."

    tot = 0
    num = 0
    valid = False
    for x, line in enumerate(input_3):
        for y, char in enumerate(line):
            if char in DIGITS:
                if num == 0:
                    num: int = first_int(line[y:])  # type: ignore
                    valid = False
                for nx, ny in neighbours(x, y, 8):
                    try:
                        if is_symbol(input_3[nx][ny]):
                            valid = True
                    except IndexError:
                        pass
            else:
                if valid:
                    tot += num
                num = 0
                valid = False

    print("Part_one:", tot)


def part_two() -> None:
    def parse_values(chords: tuple) -> tuple:
        x, y = chords
        i = x
        num = rawgrid[chords]
        while i >= 0:
            if rawgrid[(i, y)] not in DIGITS or i == 0:
                num = first_int(input_3[y][i:])
                last = i
                break
            i -= 1
        num_chords: tuple = tuple((last + nx, y) for nx in range(len(str(num))))
        return (num, num_chords)

    rawgrid = list2grid(list(input_3))

    grid: dict = {}
    for chords, val in rawgrid.items():
        if val == "*":
            grid[chords] = "*"
        elif val in DIGITS:
            grid[chords] = parse_values(chords)
        else:
            grid[chords] = None

    tot = 0
    for chords, val in grid.items():
        x, y = chords
        if val == "*":
            found = 0
            gears: list = []
            for nx, ny in neighbours(x, y, 8):
                nval = None
                try:
                    nval = grid[(nx, ny)]
                except IndexError:
                    pass

                if nval and nval != "*":
                    num, numc = nval
                    if num not in gears:
                        found += 1
                        gears.append(num)

            if found == 2:
                tot += gears[0] * gears[1]

    print("Part Two:", tot)


part_one()
part_two()
