from utils.all import *
from typing import Any, Iterator
from helpers import list2grid


class DIR(Enum):
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)


class Connection:
    __slots__ = ("d1", "d2")

    def __init__(self, d1: DIR, d2: DIR):
        self.d1 = d1
        self.d2 = d2

    def _is_pipe_dir(self, d: DIR) -> bool:
        return d == self.d1 or d == self.d2

    def next(self, d: DIR) -> DIR:
        if not self._is_pipe_dir(d):
            raise IndexError("Die Richtung ist nicht teil der Verbindung")
        return self.d1 if d == self.d2 else self.d2


PIPES = {
    "|": Connection(DIR.N, DIR.S),
    "-": Connection(DIR.E, DIR.W),
    "L": Connection(DIR.N, DIR.E),
    "J": Connection(DIR.N, DIR.W),
    "7": Connection(DIR.S, DIR.W),
    "F": Connection(DIR.S, DIR.E),
}


#  input_10 = rüad_input_line(10,sep = "\n")
input_10 = read_input_line("test_10", sep="\n")

input_10 = mapl(list, input_10)

pipe_network = []
for i in input_10:
    pipe_row = []
    for j in i:
        pipe_row.append(PIPES.get(j, j))
    pipe_network.append(pipe_row)

G = list2grid(pipe_network)
start = tuple(i for i in G.keys() if G[i] == "S")[0]
print(start)

dist = {k: INFINITY for k in G.keys()}
dist[start] = 0

for nx, ny in neighbors4(pipe_network, *start):
    cur = (nx, ny)
    while cur != start:
        if isinstance(G[cur], Connection):
            cur = G[cur].next()
