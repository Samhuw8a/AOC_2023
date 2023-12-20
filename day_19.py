from utils.all import *
from operator import lt, gt
from typing import Callable


def find_op(s: str) -> Callable:
    if s == ">":
        return gt

    elif s == "<":
        return lt

    return lambda x: None


class Filter:
    def __init__(self, s: str):
        s = s.split("{")[1].rstrip("}")
        self.s = s
        self.req = s.split(",")[:-1]
        self.default = s.split(",")[-1]

    def __repr__(self):
        return f"{self.req};{self.default}"

    def parse(self, inp: dict) -> str:
        for i in self.req:
            fil, res = i.split(":")
            var = inp[fil[0]]
            op = find_op(fil[1])
            val = int(fil[2:])
            if op(var, val):
                return res
        return self.default


def parse_group(s: str) -> dict:
    o = s.strip("{}").split(",")
    d = {x.split("=")[0]: int(x.split("=")[1]) for x in o}
    return d


input_19 = read_input_line(19, sep="\n\n")
#  input_19 = read_input_line("test_19", sep="\n\n")

rfilters, rgroups = input_19
lfilters = parse_multiline_string(rfilters, str, sep="\n")
groups = parse_multiline_string(rgroups, str, sep="\n")
groups = mapl(parse_group, groups)
filters: dict = {x.split("{")[0]: Filter(x) for x in lfilters}

tot = 0
for g in groups:
    nxt = filters["in"].parse(g)
    while nxt not in "AR":
        print(nxt)
        nxt = filters[nxt].parse(g)
    print()
    if nxt == "A":
        tot += sum(g.values())

print(tot)
