from utils.all import *
from typing import Any, Callable


def list2grid(lines: list, pred: Callable[[Any], bool] = None) -> dict:
    return {
        (y, x): val
        for y, line in enumerate(lines)
        for x, val in enumerate(line)
        if (pred(val) if pred else True)  # type:ignore
    }


class DIR(Enum):
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)


def inv_dir(d: DIR) -> DIR:
    if d == DIR.N:
        return DIR.S
    if d == DIR.S:
        return DIR.N
    if d == DIR.E:
        return DIR.W
    if d == DIR.W:
        return DIR.E
    return d


def inc_cord(cord: tuple, d: DIR) -> tuple:
    x, y = cord
    dx, dy = d.value
    return (x + dx, y + dy)


class Connection:
    __slots__ = ("d1", "d2", "string")

    def __init__(self, d1: DIR, d2: DIR, string: str = "N/A"):
        self.d1 = d1
        self.d2 = d2
        self.string = string

    def next(self, d: DIR) -> DIR:
        if d == inv_dir(self.d1):
            return self.d2
        elif d == inv_dir(self.d2):
            return self.d1
        else:
            raise IndexError

    def __repr__(self):
        return self.string


class StraightConnection(Connection):
    def next(self, d: DIR) -> DIR:
        return d


PIPES = {
    "|": StraightConnection(DIR.N, DIR.S, string="|"),
    "-": StraightConnection(DIR.E, DIR.W, string="-"),
    "L": Connection(DIR.N, DIR.E, string="L"),
    "J": Connection(DIR.N, DIR.W, string="J"),
    "7": Connection(DIR.S, DIR.W, string="7"),
    "F": Connection(DIR.S, DIR.E, string="F"),
}


input_10 = read_input_line(10, sep="\n")
#  input_10 = read_input_line("test_10", sep="\n")

input_10 = mapl(list, input_10)

pipe_network = []
for i in input_10:
    pipe_row = []
    for j in i:
        pipe_row.append(PIPES.get(j, j))
    pipe_network.append(pipe_row)

pipes = list2grid(pipe_network)
start = tuple(i for i in pipes.keys() if pipes[i] == "S")[0]

dist: defaultdict = defaultdict(lambda: INFINITY)
G: dict = {}

for c, v in pipes.items():
    if isinstance(v, str):
        G[c] = tuple()
    else:
        G[c] = (inc_cord(c, v.d1), inc_cord(c, v.d2))

start_neighb = []
for i in DIR:
    nstart = inc_cord(start, i)
    if not pipes.get(nstart):
        continue
    if isinstance(pipes[nstart], Connection):
        start_neighb.append(nstart)
G[start] = start_neighb

q = deque([(0, *start)])
visited: set = set()

while q:
    d, x, y = q.popleft()

    dist[(x, y)] = min(dist[(x, y)], d)

    if (x, y) in visited:
        continue

    print(x, y, pipes[(x, y)], d)
    visited.add((x, y))
    q.extend((d + 1, *c) for c in G[(x, y)])

print(max(dist.values()))
#  print(dist)
