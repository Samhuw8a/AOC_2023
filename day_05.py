from helpers import *


class NumRange:
    def __init__(self, values: tuple) -> None:
        self.dest = values[0]
        self.source = values[1]
        self.lenght = values[2]

    def __getitem__(self, key: int) -> int:
        return self.dest + (key - self.source)

    def __contains__(self, num: int) -> bool:
        return num >= self.source and num < self.source + self.lenght


def convert_to_next(x: int, mapping: dict) -> int:
    for conv in mapping:
        if x in conv:
            return conv[x]
    return x


input_5 = read_input_line(5, sep="\n\n")
#  input_5 = read_input_line("test_05", sep="\n\n")

input_5 = mapl(lambda x: x.split("\n"), input_5)
seeds = integers(input_5[0][0].split(":")[1])
input_5 = input_5[1:]

conversions: list = []

for line in input_5:
    line = line[1:]
    values = mapt(integers, line)
    conversion: list = []
    for value in values:
        conversion.append(NumRange(value))
    conversions.append(conversion)


def seed_to_location(seed: int) -> int:
    for mapping in conversions:
        #  print(seed)
        seed = convert_to_next(seed, mapping)
    #  print(seed)
    #  print()
    return seed


locations = mapt(seed_to_location, seeds)
print("Part One:", min(locations))
