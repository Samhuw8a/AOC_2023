from helpers import *

input_1 = read_input_line(1, sep="\n")
test_input = read_input_line("test_01", sep="\n")

WORDS = {
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "nine": 9,
    "two": 2,
    "eight": 8,
    "one": 1,
}


def extract_num_from_line(line: str) -> str:
    i = 0
    new = ""
    for i, char in enumerate(line):
        if char in DIGITS:
            new += char
        for w, n in WORDS.items():
            j = line.find(w, i)
            if j == i:
                new += str(n)
                break

    return new


def problem_1() -> None:
    tot = 0
    for line in input_1:
        nums = extract_num_from_line(line)
        print(nums[0] + nums[-1])
        num = int(nums[0] + nums[-1])
        tot += num
    print(tot)


problem_1()
#  print(extract_num_from_line(test_input[0]))
